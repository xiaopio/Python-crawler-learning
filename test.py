import os
import pprint

import requests
import re
import json

from lxml import etree

url = 'https://www.bilibili.com/video/BV1pjgbzhEPM/?spm_id_from=333.934.0.0&vd_source=85dcb05ae19afffebcb910c83dd15efe'

headers = {
    'referer': 'https://www.bilibili.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

info = re.findall('window.__playinfo__=(.*?)</script>', response.text)[0]

video_url = json.loads(info)['data']['dash']['video'][0]['baseUrl']
print(video_url)
# video_url = 'https://xy115x56x242x25xy.mcdn.bilivideo.cn:8082/v1/resource/30688283798-1-100050.m4s?agrr=0&build=0&buvid=EB1FEA78-3F5C-150C-DC9F-5D86400F926D20714infoc&bvc=vod&bw=1279944&deadline=1753450133&dl=0&e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M%3D&f=u_0_0&gen=playurlv3&lrs=37&mcdnid=50018145&mid=1286117338&nbs=1&nettype=0&og=cos&oi=0x24098a44367f0ba0e0bedcd3a466a7f7&orderid=0%2C3&os=mcdn&platform=pc&sign=5c5b4d&traceid=trzptoWWDqJCdR_0_e_N&uipk=5&uparams=e%2Cmid%2Coi%2Cnbs%2Cuipk%2Cgen%2Cdeadline%2Cplatform%2Ctrid%2Cos%2Cog&upsig=f6bb381dd1a5dd1b4139c6645ff36e7c'

audio_url = json.loads(info)['data']['dash']['audio'][0]['baseUrl']
print(audio_url)
html = etree.HTML(response.text)
filename = html.xpath('//h1/text()')[0]

print(filename)

video = requests.get(video_url, headers=headers).content
audio = requests.get(audio_url, headers=headers).content

with open(f'{filename}.mp4', 'wb') as f:
    f.write(video)
print('已下载视频部分')
with open(f'{filename}.mp3', 'wb') as f:
    f.write(audio)
print('已下载音频部分')
cmd = fr'D:\Programs\FFmpeg\ffmpeg-7.1.1\bin\ffmpeg -i {filename}.mp4 -i {filename}.mp3 -c:v copy -c:a aac -strict experimental output-{filename}.mp4'
os.system(cmd)
print('合并完成')
os.remove(f'{filename}.mp4')
os.remove(f'{filename}.mp3')
