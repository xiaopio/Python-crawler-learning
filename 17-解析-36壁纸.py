# https://www.3gbizhi.com/sjbz/index_1.html
# https://www.3gbizhi.com/meinv/index_1.html
import time
import urllib.request
import uuid

import requests
from lxml import etree
import os


def custom_requests(page):
    """
    定制请求
    :param page: 页码
    :return: 请求参数
    """
    # 手机壁纸启用
    # url = f'https://www.3gbizhi.com/meinv/index_{page}.html'
    # 电脑壁纸启用
    url = f'https://desk.3gbizhi.com/deskMV/index_{page}.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
    }

    return urllib.request.Request(url=url, headers=headers)


def get_response_data(request):
    """
    接收请求,返回响应数据
    :param request: 请求
    :return: response响应数据
    """
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


def parse_data(content):
    """
    解析网页,返回图片地址列表
    :param content: 网页数据
    :return: 图片地址列表
    """
    tree = etree.HTML(content)
    # 手机壁纸启用
    # url_list = tree.xpath('//li/a[@class="imgw"]/img/@lay-src')
    # img_name_list = tree.xpath('//a[@class="imgw"]/img/@title')
    # 电脑壁纸启用
    url_list = tree.xpath('//li/a[@class="desk imgw"]/img/@lay-src')
    img_name_list = tree.xpath('//li/a[@class="desk imgw"]/img/@alt')

    return url_list, img_name_list


def down_load(url_list, img_name_list, save_dir="images"):
    try:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        subscript = 0
        for url in url_list:
            # parsed_url = urlparse(url)
            filename = os.path.basename(img_name_list[subscript] + '.webp')
            subscript += 1
            if not filename:
                filename = str(uuid.uuid4()) + ".webp"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            save_path = os.path.join(save_dir, filename)
            with open(save_path, "wb") as f:
                f.write(response.content)
            time.sleep(1)
            print(f"下载成功！保存路径：{save_path}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP错误：{e}（可能链接无效或被拦截）")
    except requests.exceptions.ConnectionError:
        print("连接错误：无法连接到服务器（可能网络问题或被屏蔽）")
    except requests.exceptions.Timeout:
        print("超时错误：请求超时")
    except Exception as e:
        print(f"其他错误：{str(e)}")
    finally:
        print("执行成功!")


if __name__ == '__main__':
    print("==========--36壁纸--==========")
    start_page = int(input("请输入起始页码:"))
    end_page = int(input("请输入结束页码:"))
    path = input("请输入文件夹名:")
    for page in range(start_page, end_page + 1):
        request = custom_requests(page)
        content = get_response_data(request)
        url_list, img_name_list = parse_data(content)
        down_load(url_list, img_name_list, path)
    print("===========--end--===========")
