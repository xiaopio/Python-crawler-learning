# _*_ encoding: utf-8 _*_
"""
PyCharm main
2025年07月20日 15时11分40秒
by LiXiaoYang
"""

import requests
import execjs
import json
from datetime import datetime

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.xiniudata.com',
    'priority': 'u=1, i',
    'referer': 'https://www.xiniudata.com/project/lib',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'cookie': 'btoken=BPLZUAS8Z35GFBNCSWWXDZRZOBDQF3DF; utoken=Z52WACTW853UO3PV51GIDGEKR8B7EC7D; username=%E3%85%A4%E3%85%A4%E3%85%A4; export_notice=true',
}

json_data = {
    'payload': 'LBcnV1QrNXhyGnsGaBwCBgtmABYVcAZ6D3gUeA4WEGN1Zg5qdX1yCX5jdWBgCBYRcQ5+Yht+dgUXARkUARwGbXsXd3sDfhRqHBl7bhoSEAt8YnR9DXB4EAkBGQcOF38IdRlmbXsFFQACEG5gFGdnDgEeZnlrB3YebwcaC2MLfh5nF2gaUyY1MjspOzFKNHdlEDhfXlA3P1cnJ3BhdClbKSJGLF1eKTEvIyQzKxppdz5XPVpdQzo9UCJsfm8yNlQ8PwEUWUIvIjMvLHtuGi40J1U1X01QPDNLLCA1b3pnAw0fe31tfANkdmobGw9+fWJ7YXYaFn1mDnsCDwt6dBhP',
    'sig': 'E15D8F728834D06A9183D43EE2A3D012',
    'v': 1,
}

response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_company4_list/list_companies4_list_by_codes',
    headers=headers,
    json=json_data,
).json()

# print(response['d'])

with open('./demo1.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

ctx = execjs.compile(js_code)
result = ctx.call("what", response['d'])
print(result)


def parse_company_data(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>公司融资信息报告</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #2c3e50; text-align: center; }
            .company-container { margin-bottom: 30px; border: 1px solid #ddd; padding: 15px; border-radius: 5px; }
            .company-header { display: flex; align-items: center; margin-bottom: 15px; }
            .company-logo { width: 60px; height: 60px; margin-right: 15px; border-radius: 5px; object-fit: cover; }
            .company-info { flex: 1; }
            .company-name { font-size: 18px; font-weight: bold; margin: 0; }
            .company-brief { color: #7f8c8d; margin: 5px 0; }
            .tags { display: flex; flex-wrap: wrap; gap: 5px; margin: 10px 0; }
            .tag { background-color: #e0e0e0; padding: 3px 8px; border-radius: 3px; font-size: 12px; }
            .details-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }
            .detail-item { margin-bottom: 8px; }
            .detail-label { font-weight: bold; color: #34495e; }
            .funding-info { background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin-top: 10px; }
            .investors { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 10px; }
            .investor { background-color: #e3f2fd; padding: 5px 10px; border-radius: 3px; font-size: 13px; }
            .timestamp { color: #95a5a6; font-size: 12px; }
        </style>
    </head>
    <body>
        <h1>公司融资信息报告</h1>
    """

    for company in data['list']:
        # 基本信息
        name = company.get('name', 'N/A')
        brief = company.get('brief', '暂无简介')
        logo = company.get('logo', '')
        tags = ", ".join(company.get('tagNameList', []))

        # 时间转换
        establish_date = datetime.fromtimestamp(company.get('establishDate', 0) / 1000).strftime('%Y-%m-%d') \
            if company.get('establishDate') else '未知'

        # 融资信息
        funding = company.get('funding', {})
        round_name = funding.get('roundName', '未知轮次')
        funding_date = datetime.fromtimestamp(funding.get('fundingDate', 0) / 1000).strftime('%Y-%m-%d') \
            if funding.get('fundingDate') else '未知'

        # 解析fundingDesc
        funding_desc = {}
        if funding.get('fundingDesc'):
            try:
                funding_desc = json.loads(funding['fundingDesc'])
            except:
                pass

        money = funding_desc.get('money', '未披露')
        post_money = funding_desc.get('postMoney', '未披露')
        ratio = funding_desc.get('ratio', '未披露')
        investor_list = funding_desc.get('investorList', [])

        # 构建HTML
        html_content += f"""
        <div class="company-container">
            <div class="company-header">
                <img src="{logo}" alt="{name} Logo" class="company-logo" onerror="this.style.display='none'">
                <div class="company-info">
                    <h2 class="company-name">{name}</h2>
                    <p class="company-brief">{brief}</p>
                </div>
            </div>

            <div class="tags">
                {''.join([f'<span class="tag">{tag}</span>' for tag in company.get('tagNameList', [])])}
            </div>

            <div class="details-grid">
                <div class="detail-item">
                    <span class="detail-label">成立日期：</span>
                    <span>{establish_date}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">所在地：</span>
                    <span>{company.get('locationName', '未知')}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">融资轮次：</span>
                    <span>{round_name}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">融资时间：</span>
                    <span>{funding_date}</span>
                </div>
            </div>

            <div class="funding-info">
                <div class="detail-item">
                    <span class="detail-label">融资金额：</span>
                    <span>{money}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">投后估值：</span>
                    <span>{post_money}</span>
                </div>
                <div class="detail-item">
                    <span class="detail-label">投资占比：</span>
                    <span>{ratio}{'%' if isinstance(ratio, (int, float)) else ''}</span>
                </div>

                <div class="detail-item">
                    <span class="detail-label">投资方：</span>
                    <div class="investors">
                        {''.join([f'<span class="investor">{inv.get("name")}</span>' for inv in investor_list])}
                        {'' if investor_list else '<span>未披露</span>'}
                    </div>
                </div>
            </div>
        </div>
        """

    html_content += """
    </body>
    </html>
    """
    return html_content


# 生成HTML内容
html_output = parse_company_data(result)

# 保存到文件
with open('company_funding_report.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("HTML文件已生成: company_funding_report.html")
