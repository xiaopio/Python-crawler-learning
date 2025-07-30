import re
from datetime import datetime, timedelta


def time_to_ms(time_str):
    """将SRT时间格式（00:00:00,240）转换为毫秒数"""
    # 替换逗号为点，适配datetime解析（如00:00:00,240 → 00:00:00.240）
    time_str = time_str.replace(',', '.')
    # 解析时间（时:分:秒.毫秒）
    dt = datetime.strptime(time_str, "%H:%M:%S.%f")
    # 转换为总毫秒数
    return int((dt.hour * 3600 + dt.minute * 60 + dt.second) * 1000 + dt.microsecond / 1000)


def ms_to_time(ms):
    """将毫秒数转换为SRT时间格式（00:00:00,240）"""
    # 计算时、分、秒、毫秒
    hours = ms // 3600000
    ms %= 3600000
    minutes = ms // 60000
    ms %= 60000
    seconds = ms // 1000
    ms %= 1000
    # 格式化为两位数时/分/秒，三位数毫秒（补零）
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{ms:03d}"


def parse_srt(srt_content):
    """解析SRT内容为条目列表，每个条目包含：序号、开始时间(ms)、结束时间(ms)、文本"""
    # 按空行分割条目（SRT格式用空行分隔条目）
    blocks = re.split(r'\n\s*\n', srt_content.strip())
    entries = []
    for block in blocks:
        lines = [line.strip() for line in block.split('\n') if line.strip()]
        if len(lines) < 2:
            continue  # 跳过无效条目
        # 提取序号（可能为数字字符串）
        index = lines[0]
        # 提取时间轴（如"00:00:00,240 --> 00:00:04,319"）
        time_line = lines[1]
        start_str, end_str = re.split(r'\s*-->\s*', time_line)
        # 转换为毫秒
        start_ms = time_to_ms(start_str)
        end_ms = time_to_ms(end_str)
        # 提取文本（可能有多行，合并为一行）
        text = ' '.join(lines[2:]) if len(lines) > 2 else ''
        entries.append({
            'index': index,
            'start_ms': start_ms,
            'end_ms': end_ms,
            'text': text
        })
    # 按开始时间排序（确保时间顺序正确）
    return sorted(entries, key=lambda x: x['start_ms'])


def fix_overlapping(entries):
    """修复时间轴重叠：前一条结束时间不晚于后一条开始时间"""
    for i in range(len(entries) - 1):
        current = entries[i]
        next_entry = entries[i + 1]
        # 如果当前条目的结束时间晚于下一条的开始时间，强制调整
        if current['end_ms'] > next_entry['start_ms']:
            current['end_ms'] = next_entry['start_ms']
    return entries


def process_punctuation(text):
    """处理标点符号：
    - 开头/结尾的标点直接删除
    - 句中的标点替换为两个空格
    """
    if not text:
        return text  # 空文本直接返回
    # 定义需要处理的标点（可根据需求补充）
    punctuation = ',.!?;:"\'()[]{}<>、，。！？；：“”‘’（）【】《》'

    # 去除开头的标点
    start_idx = 0
    while start_idx < len(text) and text[start_idx] in punctuation:
        start_idx += 1
    # 去除结尾的标点
    end_idx = len(text) - 1
    while end_idx >= 0 and text[end_idx] in punctuation:
        end_idx -= 1
    # 截取处理后的中间部分
    if start_idx > end_idx:
        return ''  # 全是标点的情况，返回空
    trimmed = text[start_idx:end_idx + 1]

    # 句中的标点替换为两个空格
    processed = []
    for char in trimmed:
        if char in punctuation:
            processed.append('  ')  # 两个空格
        else:
            processed.append(char)
    return ''.join(processed)


def generate_srt(entries):
    """将处理后的条目转换为SRT格式字符串"""
    srt_lines = []
    # 重新编号（确保序号连续）
    for i, entry in enumerate(entries, 1):
        srt_lines.append(str(i))  # 序号（重新从1开始）
        # 时间轴（开始 --> 结束）
        start_time = ms_to_time(entry['start_ms'])
        end_time = ms_to_time(entry['end_ms'])
        srt_lines.append(f"{start_time} --> {end_time}")
        # 处理后的文本
        srt_lines.append(process_punctuation(entry['text']))
        srt_lines.append('')  # 条目间空行分隔
    # 移除最后一个空行
    return '\n'.join(srt_lines).rstrip()


def main(input_path, output_path):
    """主函数：读取SRT → 解析 → 修复重叠 → 处理标点 → 生成新SRT"""
    with open(input_path, 'r', encoding='utf-8') as f:
        srt_content = f.read()

    # 解析并处理
    entries = parse_srt(srt_content)
    entries = fix_overlapping(entries)
    new_srt = generate_srt(entries)

    # 写入输出文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_srt)
    print(f"处理完成，输出文件：{output_path}")


if __name__ == '__main__':
    # 输入文件路径和输出文件路径（可修改）
    input_srt = f'D:\\admin\Videos\YouTube\\1.srt'  # 原始SRT文件
    output_srt = 'output.srt'  # 处理后的SRT文件
    main(input_srt, output_srt)