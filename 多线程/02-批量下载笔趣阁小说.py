import os
import threading
import time
import re
from glob import glob
from urllib.parse import urlparse

import requests
from lxml import etree
from queue import Queue

gen_url_done = False


def gen_urls(url, q):
    headers = {
        'referer': 'https://m.bqgl.cc/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'cookie': 'closead=true',
    }
    global gen_url_done
    response = requests.get(url=url, headers=headers).text
    # print(response)
    html = etree.HTML(response)
    links = html.xpath('//dl/dd/a/@href')
    titles = html.xpath('//dl/dd/a/text()')
    del (links[0])
    del (titles[0])
    for i in range(len(titles)):
        # i从0开始，所以序号需要+1
        titles[i] = f"{i + 1}-{titles[i]}"
    for i in range(len(links)):
        # i从0开始，所以序号需要+1
        links[i] = 'https://m.a897756d.cfd' + links[i]
    # print(links)
    new_links, new_titles = expand_links_and_titles(links, titles)
    # print(new_titles, new_titles)
    for i in range(len(new_links)):
        book = (new_titles[i], new_links[i])
        q.put(book)
    gen_url_done = True


def check_link_exists(url):
    """检查链接是否存在（简单 HEAD 请求验证）"""
    try:
        # 使用HEAD请求更高效，仅获取响应头
        response = requests.head(url, allow_redirects=True, timeout=10)
        # 200-299状态码表示链接有效
        return 200 <= response.status_code < 300
    except:
        return False


def expand_links_and_titles(original_links, original_titles):
    """扩展链接列表，添加存在的子链接，并生成对应标题"""
    expanded_links = []
    expanded_titles = []

    for main_link, main_title in zip(original_links, original_titles):
        # 添加主链接和对应标题
        expanded_links.append(main_link)
        expanded_titles.append(main_title)

        # 解析主链接，提取基础部分（如1.html -> 1）
        parsed = urlparse(main_link)
        main_part = parsed.path.split('/')[-1].rsplit('.', 1)[0]  # 提取"1"、"2"等

        # 检查可能的子链接（1_1.html, 1_2.html...）
        sub_index = 2
        while True:
            # 构建子链接
            sub_link = main_link.replace(f"{main_part}.html", f"{main_part}_{sub_index}.html")
            # print(sub_link)
            # 检查子链接是否存在
            if check_link_exists(sub_link):
                # 生成对应标题（原标题_序号）
                sub_title = f"{main_title}_{sub_index}"

                # 添加到扩展列表
                expanded_links.append(sub_link)
                expanded_titles.append(sub_title)

                sub_index += 1
            else:
                # 子链接不存在时停止检查
                break

    return expanded_links, expanded_titles


def downloads(q, path):
    headers = {
        'referer': 'https://m.bqgl.cc/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'cookie': 'closead=true',
    }
    while True:
        if q.empty() and gen_url_done:
            print('已完成全部下载')
            break
        else:
            book = q.get()
            title, url = book
            # print(title, url)
            response = requests.get(url=url, headers=headers).text
            # print(response)
            html = etree.HTML(response)
            content = html.xpath('//div[@id="chaptercontent"]/text()')
            content = "".join(content).strip().replace('\u3000\u3000', '\n').replace('请收藏：https://m.a897756d.cfd',
                                                                                     '')
            # print(content)
            # title = html.xpath('//span[@class="title"]/text()')[0]
            # title = title.split('）', 1)[1].lstrip()
            # print(title)
            #
            with open(f'{path}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title + '\n\n')
                f.write(content + '\n\n')
                print(f'{threading.current_thread().name}已完成...{title}的下载')


def combine_files(path, timeout=None, expected_sections=None):
    """
    带结束判断的文件合并方法
    :param path: 文件存放目录
    :param timeout: 超时时间（秒），超过此时长未检测到新文件则终止，默认5分钟
    :param expected_sections: 预期的主节总数（如已知共100章，可指定为100），达到则终止
    """
    os.makedirs(path, exist_ok=True)
    temp_dir = os.path.join(path, "temp_merged")
    os.makedirs(temp_dir, exist_ok=True)
    final_output = os.path.join(path, "最终合并.txt")

    main_section_status = {}  # {主节编号: (是否合并, 最大分节号)}
    last_final_merged = 0
    last_new_file_time = time.time()  # 最后一次检测到新文件的时间
    lock = threading.Lock()

    print(f"开始合并，超时时间: {timeout}秒，预期主节数: {expected_sections or '未知'}")

    try:
        while True:
            # 检查超时：超过指定时间未检测到新文件则终止
            if time.time() - last_new_file_time > timeout:
                print(f"\n超时未检测到新文件（{timeout}秒），合并终止")
                break

            # 检查是否达到预期主节总数
            if expected_sections and last_final_merged >= expected_sections:
                print(f"\n已完成所有预期主节（共{expected_sections}章），合并终止")
                break

            # 扫描所有文件
            all_files = [f for f in glob(os.path.join(path, "*.txt"))
                         if os.path.basename(f) != "最终合并.txt"]
            current_file_count = len(all_files)

            # 按主节分组
            section_groups = {}
            for file in all_files:
                filename = os.path.basename(file)
                match = re.match(r"^(\d+)-", filename)
                if not match:
                    continue
                main_num = match.group(1)

                if main_num not in section_groups:
                    section_groups[main_num] = {"main": None, "subsections": []}

                if "_" in filename:
                    sub_match = re.search(r"_(\d+)\.txt$", filename)
                    if sub_match:
                        sub_num = int(sub_match.group(1))
                        section_groups[main_num]["subsections"].append((sub_num, file))
                else:
                    section_groups[main_num]["main"] = file

            # 处理分节合并到主节
            new_content_detected = False
            for main_num, group in section_groups.items():
                if not group["main"]:
                    continue

                group["subsections"].sort(key=lambda x: x[0])
                sub_numbers = [num for num, _ in group["subsections"]]
                max_sub = max(sub_numbers) if sub_numbers else 0
                current_status = main_section_status.get(main_num, (False, 0))

                # 检测到新内容（未合并过或有新分节）
                if not current_status[0] or max_sub > current_status[1]:
                    new_content_detected = True
                    last_new_file_time = time.time()  # 更新最后活动时间

                    with lock:
                        temp_file = os.path.join(temp_dir, f"{main_num}-合并临时文件.txt")
                        with open(temp_file, "w", encoding="utf-8") as out_f:
                            # 写入主节内容
                            with open(group["main"], "r", encoding="utf-8") as main_f:
                                out_f.write(main_f.read())
                                out_f.write("\n\n")

                            # 写入分节内容
                            for sub_num, sub_file in group["subsections"]:
                                with open(sub_file, "r", encoding="utf-8") as sub_f:
                                    out_f.write(f"【分节 {sub_num}】\n")
                                    out_f.write(sub_f.read())
                                    out_f.write("\n\n")

                        main_section_status[main_num] = (True, max_sub)
                        print(f"已合并主节 {main_num}（分节数: {max_sub}）")

            # 合并主节到最终文件
            processed_mains = [int(num) for num, status in main_section_status.items() if status[0]]
            processed_mains.sort()

            if processed_mains:
                next_main = last_final_merged + 1
                if next_main in processed_mains:
                    new_content_detected = True
                    last_new_file_time = time.time()

                    with lock:
                        temp_file = os.path.join(temp_dir, f"{next_main}-合并临时文件.txt")
                        if os.path.exists(temp_file):
                            with open(final_output, "a", encoding="utf-8") as final_f:
                                with open(temp_file, "r", encoding="utf-8") as temp_f:
                                    final_f.write(f"【part-{next_main}】\n")
                                    final_f.write(temp_f.read())
                                    final_f.write("\n\n")

                            last_final_merged = next_main
                            print(f"已合并到最终文件：第 {next_main} 章")

            # 如果没有检测到新内容，短暂休眠
            if not new_content_detected:
                time.sleep(2)

    except KeyboardInterrupt:
        print(f"\n用户中断，当前已合并到第 {last_final_merged} 章")
    except Exception as e:
        print(f"合并出错：{str(e)}")
    finally:
        print(f"\n合并结束，共合并 {last_final_merged} 个主节")
        print(f"最终文件路径：{final_output}")


def main():
    url = 'https://m.a897756d.cfd/book/64673/list.html'
    path = r'D:\Code\PyCharm\Python爬虫\books'
    q = Queue(maxsize=2000)
    th1 = threading.Thread(target=gen_urls, args=(url, q))
    th1.start()
    for i in range(3):
        th2 = threading.Thread(target=downloads, args=(q, path), name=f'线程{i}')
        th2.start()
    th3 = threading.Thread(target=combine_files, args=(path, int(300), int(10000)))
    th3.start()


if __name__ == '__main__':
    main()
