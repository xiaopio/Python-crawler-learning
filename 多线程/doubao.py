import os
import threading
import time
import re
import shutil
from glob import glob
from urllib.parse import urlparse

import requests
from lxml import etree
from queue import Queue

gen_url_done = False
expected_sections_num = 0  # 预期主节总数


def gen_urls(url, q):
    global gen_url_done, expected_sections_num
    headers = {
        'referer': 'https://m.bqgl.cc/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'cookie': 'closead=true',
    }
    try:
        response = requests.get(url=url, headers=headers).text
        html = etree.HTML(response)
        links = html.xpath('//dl/dd/a/@href')[:10]
        titles = html.xpath('//dl/dd/a/text()')
        if len(links) > 0 and len(titles) > 0:
            del links[0]
            del titles[0]

        # 记录预期主节总数（原始主节数量）
        expected_sections_num = len(titles)

        # 生成带序号的标题和完整链接
        for i in range(len(titles)):
            titles[i] = f"{i + 1}-{titles[i]}"
        for i in range(len(links)):
            links[i] = 'https://m.a897756d.cfd' + links[i]

        # 扩展子链接
        expanded_links, expanded_titles = expand_links_and_titles(links, titles)
        for title, link in zip(expanded_titles, expanded_links):
            q.put((title, link))

        print(f"URL生成完成，共{len(expanded_links)}个文件（含分节）")
    except Exception as e:
        print(f"生成URL出错：{e}")
    finally:
        gen_url_done = True


def check_link_exists(url):
    """检查子链接是否存在"""
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
        }
        response = requests.head(url, headers=headers, allow_redirects=True, timeout=5)
        return 200 <= response.status_code < 300
    except:
        return False


def expand_links_and_titles(original_links, original_titles):
    """扩展子链接（从_2开始）"""
    expanded_links = []
    expanded_titles = []
    for main_link, main_title in zip(original_links, original_titles):
        expanded_links.append(main_link)
        expanded_titles.append(main_title)

        # 提取主链接基础部分（如1.html -> 1）
        parsed = urlparse(main_link)
        main_part = parsed.path.split('/')[-1].rsplit('.', 1)[0]

        # 检查子链接（从_2开始）
        sub_index = 2
        while True:
            sub_link = main_link.replace(f"{main_part}.html", f"{main_part}_{sub_index}.html")
            if check_link_exists(sub_link):
                expanded_links.append(sub_link)
                expanded_titles.append(f"{main_title}_{sub_index}")
                sub_index += 1
            else:
                break
    return expanded_links, expanded_titles


def downloads(q, path):
    """下载文件线程"""
    headers = {
        'referer': 'https://m.bqgl.cc/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'cookie': 'closead=true',
    }
    try:
        while True:
            if q.empty() and gen_url_done:
                print(f"{threading.current_thread().name}下载完成")
                break
            try:
                title, url = q.get(timeout=5)  # 超时退出，避免无限阻塞
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()

                # 解析内容
                html = etree.HTML(response.text)
                content = html.xpath('//div[@id="chaptercontent"]/text()')
                content = "".join(content).strip().replace('\u3000\u3000', '\n').replace(
                    '请收藏：https://m.a897756d.cfd', ''
                )

                # 保存文件
                file_path = os.path.join(path, f"{title}.txt")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(title + '\n\n')
                    f.write(content + '\n\n')
                print(f"{threading.current_thread().name} 已下载：{title}")
                q.task_done()
            except Exception as e:
                print(f"{threading.current_thread().name} 下载出错：{e}")
                q.task_done()
    except Exception as e:
        print(f"{threading.current_thread().name} 线程异常：{e}")


def delete_downloaded_files(path):
    """删除下载的原始文件和临时合并文件"""
    try:
        # 1. 删除原始下载文件（主节和分节）
        original_files = [f for f in glob(os.path.join(path, "*.txt"))
                          if os.path.basename(f) != "最终合并.txt"]
        for file in original_files:
            os.remove(file)
            print(f"已删除原始文件：{os.path.basename(file)}")

        # 2. 删除临时合并目录及内容
        temp_dir = os.path.join(path, "temp_merged")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"已删除临时目录：{temp_dir}")

    except Exception as e:
        print(f"删除文件时出错：{e}（部分文件可能被占用，建议手动清理）")


def combine_files(path, timeout=300):
    """合并文件并在完成后删除原始文件"""
    os.makedirs(path, exist_ok=True)
    temp_dir = os.path.join(path, "temp_merged")
    os.makedirs(temp_dir, exist_ok=True)
    final_output = os.path.join(path, "最终合并.txt")

    main_section_status = {}  # {主节编号: (是否合并, 最大分节号)}
    last_final_merged = 0
    last_new_file_time = time.time()
    lock = threading.Lock()
    global expected_sections_num

    print(f"开始合并，超时时间：{timeout}秒，预期主节数：{expected_sections_num}")

    try:
        while True:
            # 超时判断
            if time.time() - last_new_file_time > timeout:
                print(f"\n超时未检测到新文件，合并终止")
                break

            # 完成预期主节数判断
            if expected_sections_num and last_final_merged >= expected_sections_num:
                print(f"\n已完成所有预期主节（共{expected_sections_num}章），合并终止")
                break

            # 扫描所有文件（排除最终合并文件）
            all_files = [f for f in glob(os.path.join(path, "*.txt"))
                         if os.path.basename(f) != "最终合并.txt"]

            # 按主节分组
            section_groups = {}
            for file in all_files:
                filename = os.path.basename(file)
                # 提取主节编号（如"1-标题.txt"中的1）
                match = re.match(r"^(\d+)-", filename)
                if not match:
                    continue
                main_num = int(match.group(1))

                if main_num not in section_groups:
                    section_groups[main_num] = {"main": None, "subsections": []}

                # 区分主节和分节
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
                    continue  # 主节文件不存在则跳过

                # 排序分节
                group["subsections"].sort(key=lambda x: x[0])
                sub_numbers = [num for num, _ in group["subsections"]]
                max_sub = max(sub_numbers) if sub_numbers else 0
                current_status = main_section_status.get(main_num, (False, 0))

                # 检测到新内容（未合并或有新分节）
                if not current_status[0] or max_sub > current_status[1]:
                    new_content_detected = True
                    last_new_file_time = time.time()

                    with lock:
                        # 合并主节+分节到临时文件
                        temp_file = os.path.join(temp_dir, f"{main_num}-临时合并.txt")
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
                        print(f"已合并主节 {main_num}（分节数：{max_sub}）")

            # 合并主节到最终文件
            processed_mains = [num for num, status in main_section_status.items() if status[0]]
            processed_mains.sort()
            available_mains = [num for num in processed_mains if num > last_final_merged]

            if available_mains:
                next_main = min(available_mains)  # 按顺序合并下一个主节
                new_content_detected = True
                last_new_file_time = time.time()

                with lock:
                    temp_file = os.path.join(temp_dir, f"{next_main}-临时合并.txt")
                    if os.path.exists(temp_file):
                        with open(final_output, "a", encoding="utf-8") as final_f:
                            with open(temp_file, "r", encoding="utf-8") as temp_f:
                                final_f.write(f"【第 {next_main} 章】\n")
                                final_f.write(temp_f.read())
                                final_f.write("\n\n")
                        last_final_merged = next_main
                        print(f"已合并到最终文件：第 {next_main} 章")

            if not new_content_detected:
                time.sleep(2)

    except KeyboardInterrupt:
        print(f"\n用户中断，当前已合并到第 {last_final_merged} 章")
    except Exception as e:
        print(f"合并出错：{e}")
    finally:
        print(f"\n合并结束，共合并 {last_final_merged} 个主节")
        print(f"最终文件路径：{final_output}")

        # 合并完成后删除原始文件和临时文件
        print("\n开始清理原始文件和临时文件...")
        delete_downloaded_files(path)


def main():
    url = 'https://m.a897756d.cfd/book/64673/list.html'
    path = r'D:\Code\PyCharm\Python爬虫\books'
    q = Queue(maxsize=2000)

    # 1. 启动URL生成线程
    th1 = threading.Thread(target=gen_urls, args=(url, q))
    th1.start()
    th1.join()  # 等待URL生成完成（确保获取预期主节数）

    # 2. 启动下载线程（3个）
    for i in range(3):
        th2 = threading.Thread(target=downloads, args=(q, path), name=f'下载线程{i + 1}')
        th2.daemon = True  # 主程序退出时自动结束
        th2.start()

    # 3. 启动合并线程
    th3 = threading.Thread(target=combine_files, args=(path,), kwargs={"timeout": 300})
    th3.start()
    th3.join()  # 等待合并完成

    print("所有任务已结束")


if __name__ == '__main__':
    main()