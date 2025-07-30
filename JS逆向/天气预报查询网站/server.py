import json
import csv
import requests
from flask import Flask, render_template, request
from typing import List, Dict, Optional

app = Flask(__name__)


# **location**温度**temp**天气**desc**!
@app.route('/')  # 绑定处理函数
def index_url():
    location = '北京'
    location, temp, desc = get_weather(location)
    print(location, temp, desc)
    # location = '北京'
    # temp = '23'
    # desc = '小雨'
    # with open('templates/index.html', 'r', encoding='utf-8') as f:
    #     content = f.read()
    # content = content.replace('**location**', location).replace('**temp**', temp).replace('**desc**', desc)
    # return content

    return render_template('index.html', location=location, temp=temp, desc=desc)
    # pass


@app.route('/get_data')
def get_data():
    location = request.args.get('location')
    location, temp, desc = get_weather(location)
    msg = '请求成功'
    sender_data = {'msg': msg, 'data': {'location': location, 'temp': temp, 'desc': desc}}
    sender_str = json.dumps(sender_data)
    return sender_str


def get_weather(location):
    local_code = get_main_city_id(location, 'static/China-City-List-latest.csv')
    if local_code == None:
        local_code = 101010100
    url = f'https://mn6yvv3d74.re.qweatherapi.com/v7/weather/now?location={local_code}'
    headers = {
        'X-QW-Api-Key': '1f4de055b9fd45eaad3e9586e022ff41'
    }
    response = requests.get(url=url, headers=headers).text
    data = json.loads(response)

    if data['code'] == '200':
        print('查询成功!')
        if local_code == 101010100:
            return '北京', data['now']['temp'], data['now']['text']
        return location, data['now']['temp'], data['now']['text']
    else:
        # return render_template('index.html', location=None, temp=None, desc=None)
        print('查询失败!')


def get_location_ids(
        location_name: str,
        csv_file_path: str,
        adm1_name: Optional[str] = None  # 可选参数：省份/直辖市名称，用于精确匹配
) -> List[Dict[str, str]]:
    """
    根据地区中文名从CSV文件中获取对应的Location_ID及相关信息

    参数:
        location_name: 要查询的地区中文名（如"北京"、"海淀"）
        csv_file_path: CSV文件的路径
        adm1_name: 可选，省份/直辖市名称（如"北京市"），用于区分重名地区

    返回:
        包含匹配结果的字典列表，每个字典包含Location_ID、Location_Name_ZH等信息
        如果未找到匹配结果，返回空列表
    """
    results = []

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        # 跳过首行注释（"China-City-List v202506200,,,,,,,,,,,,,"）
        next(file)

        # 读取列名行
        reader = csv.DictReader(file)

        for row in reader:
            # 精确匹配地区名称
            if row['Location_Name_ZH'] == location_name:
                # 如果指定了省份/直辖市，进一步过滤
                if adm1_name is None or row['Adm1_Name_ZH'] == adm1_name:
                    # 提取需要的信息
                    result = {
                        'Location_ID': row['Location_ID'],
                        'Location_Name_ZH': row['Location_Name_ZH'],
                        'Adm1_Name_ZH': row['Adm1_Name_ZH'],  # 所属省份/直辖市
                        'Adm2_Name_ZH': row['Adm2_Name_ZH'],  # 所属市/区
                        'Latitude': row['Latitude'],
                        'Longitude': row['Longitude']
                    }
                    results.append(result)

    return results


def get_main_city_id(location_name: str, csv_file_path: str) -> Optional[str]:
    """
    获取主要城市的Location_ID（通常是行政中心）

    参数:
        location_name: 城市中文名
        csv_file_path: CSV文件路径

    返回:
        主要城市的Location_ID，如果未找到返回None
    """
    # 先尝试精确匹配城市名，同时匹配所属行政区域
    matches = get_location_ids(location_name, csv_file_path, adm1_name=location_name + '市')

    # 如果没有找到，尝试不限制行政区域的匹配
    if not matches:
        matches = get_location_ids(location_name, csv_file_path)

    # 返回第一个匹配结果（通常是主城市ID）
    return matches[0]['Location_ID'] if matches else None


if __name__ == '__main__':
    # location = input('请输入地区名:')
    # index_url(location)
    # 仅使用本地地址和默认端口
    app.run(host='127.0.0.1', port=8888, debug=True)
