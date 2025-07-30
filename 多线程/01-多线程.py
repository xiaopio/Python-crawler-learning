import threading
import time


def singing(name):
    print(f'{name}开始唱歌')
    time.sleep(2)
    print('结束唱歌')


def dancing(name):
    print(f'{name}开始跳舞')
    time.sleep(2)
    print('结束跳舞')


if __name__ == '__main__':
    start_time = time.time()
    th1 = threading.Thread(target=singing, args=('杰伦',))
    # singing('杰伦')
    th2 = threading.Thread(target=dancing('俊杰'))
    # dancing('俊杰')
    th1.start()
    th2.start()
    end_time = time.time()
    print(f'共耗时:{end_time - start_time}')
