import asyncio
import time


# 定义协程函数
async def task1():
    print("任务1开始")
    await asyncio.sleep(1)  # 模拟I/O操作
    print("任务1结束")
    return "任务1结果"


async def task2():
    print("任务2开始")
    await asyncio.sleep(2)  # 模拟I/O操作
    print("任务2结束")
    return "任务2结果"


# 主协程
async def main():
    start_time = time.time()

    # 并发执行两个任务
    result1, result2 = await asyncio.gather(task1(), task2())

    end_time = time.time()
    print(f"总耗时: {end_time - start_time:.2f}秒")
    print(f"结果: {result1}, {result2}")


# 运行事件循环
if __name__ == "__main__":
    asyncio.run(main())
