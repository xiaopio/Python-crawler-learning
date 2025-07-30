import time

import undetected_chromedriver as uc

# 保存原始 quit 方法
_original_quit = uc.Chrome.quit


def _safe_quit(self, *args, **kwargs):
    try:
        _original_quit(self, *args, **kwargs)
    except Exception:
        pass


uc.Chrome.quit = _safe_quit

# 屏蔽 __del__ 再次调用
uc.Chrome.__del__ = lambda self: None


def run():
    opt = uc.ChromeOptions()
    # opt.headless = True
    browser = uc.Chrome(options=opt,version_main='138', browser_executable_path='./chromedriver.exe')
    browser.get('https://www.taobao.com/')
    time.sleep(2)
    title = browser.title
    print(title)
    browser.quit()  # 安全调用


if __name__ == '__main__':
    run()

# asyncio + pyppeteer 或 Playwright


# C:\Program Files\Google\Chrome\Application
