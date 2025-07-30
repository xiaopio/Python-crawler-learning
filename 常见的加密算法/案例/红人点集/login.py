import requests

headers = {
    'sec-ch-ua-platform': '"Windows"',
    'Referer': '',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'Content-Type': 'application/json',
    'sec-ch-ua-mobile': '?0',
}

json_data = {
    'phoneNum': '18874573695',
    'pwd': 'e10adc3949ba59abbe56e057f20f883e',
    't': 1753843505991,
    'tenant': 1,
    'sig': '56429ff37639e56c4defc6ffc8ad0e80',
}

response = requests.post('https://user.hrdjyun.com/wechat/phonePwdLogin', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"phoneNum":"18874573695","pwd":"e10adc3949ba59abbe56e057f20f883e","t":1753843505991,"tenant":1,"sig":"56429ff37639e56c4defc6ffc8ad0e80"}'
response = requests.post('https://user.hrdjyun.com/wechat/phonePwdLogin', headers=headers, json=json_data)

print(response.json())