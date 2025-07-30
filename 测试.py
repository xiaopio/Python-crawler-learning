import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# 自定义字符集（按明亮度从高到低排序，空格最亮，'吕'最暗）
ASCII_CHARS = [" ", "一", "二", "三", "十", "口", "日", "目", "品", "㗊", "吕"]

# 输出视频参数
OUTPUT_WIDTH = 80  # 字符画宽度（字符数）
OUTPUT_HEIGHT = 40  # 字符画高度（字符数）
FPS = 24  # 输出视频帧率
FONT_SIZE = 12  # 字体大小
FONT_PATH = "arial.ttf"  # 替换为系统字体路径（如 Windows 的 "arial.ttf" 或 Linux 的 "/usr/share/fonts/truetype/arial.ttf"）

# 加载字体（使用系统默认字体，无需严格等宽）
try:
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
except IOError:
    # 如果指定字体不存在，回退到系统默认字体
    font = ImageFont.load_default()
    print(f"警告：字体文件 {FONT_PATH} 不存在，使用系统默认字体")

# 计算字符的宽高（非等宽字体，不同字符宽度可能不同，这里取平均宽度）
# 注意：非等宽字体下，字符宽度可能不一致，会导致排版错位
bbox = font.getbbox(" ")
char_width = bbox[2] - bbox[0]
char_height = bbox[3] - bbox[1]

# 输出视频的尺寸（非等宽字体下，尺寸为近似值，可能有错位）
VIDEO_WIDTH = OUTPUT_WIDTH * char_width
VIDEO_HEIGHT = OUTPUT_HEIGHT * char_height

# 初始化视频写入器
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter(
    "output.mp4", fourcc, FPS, (VIDEO_WIDTH, VIDEO_HEIGHT)
)


def frame_to_ascii(frame):
    """
    将视频帧转换为字符画图像（无需等宽字体）
    :param frame: 视频帧（OpenCV 的 BGR 格式）
    :return: 字符画图像（RGB 格式）
    """
    # 将 BGR 转换为 RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 转换为 Pillow 图像
    img = Image.fromarray(frame_rgb)

    # 调整图像大小
    img = img.resize((OUTPUT_WIDTH, OUTPUT_HEIGHT), Image.Resampling.LANCZOS)

    # 转换为灰度图像
    img_gray = img.convert("L")

    # 生成字符画
    ascii_frame = []
    for y in range(OUTPUT_HEIGHT):
        line = ""
        for x in range(OUTPUT_WIDTH):
            # 获取灰度值
            brightness = img_gray.getpixel((x, y))

            # 根据灰度值映射到字符集
            # 亮度范围: 0 (暗) -> 255 (亮)
            # 字符集索引: 0 (亮) -> len(ASCII_CHARS)-1 (暗)
            idx = int((brightness / 255) * (len(ASCII_CHARS) - 1))
            line += ASCII_CHARS[idx]
        ascii_frame.append(line)

    # 渲染字符画为图像（非等宽字体）
    return render_ascii_image(ascii_frame)


def render_ascii_image(ascii_frame):
    """
    将字符画渲染为图像（非等宽字体）
    :param ascii_frame: 字符画文本
    :return: 渲染后的图像（RGB 格式）
    """
    # 创建黑色背景图像
    img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), color=(0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 逐行渲染字符（非等宽字体，字符宽度可能不一致）
    x_pos = 0  # 当前字符的 X 坐标
    for y, line in enumerate(ascii_frame):
        for char in line:
            # 绘制字符（白色）
            draw.text((x_pos, y * char_height), char, font=font, fill=(255, 255, 255))
            # 更新 X 坐标（非等宽字体，需要计算字符宽度）
            bbox = font.getbbox(char)
            char_width_current = bbox[2] - bbox[0]
            x_pos += char_width_current
        x_pos = 0  # 换行后重置 X 坐标

    return img


def main(video_path):
    # 打开视频
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("无法打开视频文件")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break  # 视频结束

            # 转换为字符画图像
            ascii_img = frame_to_ascii(frame)

            # 转换为 OpenCV 格式（BGR）
            ascii_frame_cv = cv2.cvtColor(np.array(ascii_img), cv2.COLOR_RGB2BGR)

            # 写入视频
            video_writer.write(ascii_frame_cv)

            # 显示进度（可选）
            print(f"处理帧: {cap.get(cv2.CAP_PROP_POS_FRAMES)}", end="\r")

    except KeyboardInterrupt:
        print("\n手动中断处理")
    finally:
        # 释放资源
        cap.release()
        video_writer.release()
        print("视频已保存为 output.mp4")


if __name__ == "__main__":
    video_path = r"D:\admin\Pictures\Camera Roll\1.mp4"  # 替换为你的视频路径
    main(video_path)