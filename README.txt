1. 创建爬虫项目      scrapy startproject 项目名
                    注意:项目的名字不允许使用数字开头 也不能包含中文
2. 创建爬虫文件
                    要在spiders文件夹下面去创建爬虫文件
                    cd 项目名\项目名\spiders

                    创建爬虫文件
                    scrapy genspider 爬虫文件名 要爬取的网页
                    eg: scrapy genspider baidu www.baidu.com
                    一般情况下不需要添加http协议
                    因为start_url的值是根据allowed_domains自动修改的
3. 运行爬虫代码
                    scrapy crawl 爬虫文件名
                    eg: scrapy crawl baidu

4. scrapy项目的结构
    项目名字
        项目名字
            spiders文件夹(存储的是爬虫文件)
                init
                自定义的爬虫文件    核心功能文件
            init
            items       (定义数据结构的地方 爬取的数据都包含哪些)
            middleware  (中间件 代理)
            pipelines   (管道 用来处理下载的数据)
            settings    (配置文件 robots协议 ua定义等)
5. response的属性和方法
        response.text               获取的是响应的字符串
        response.body               获取的是响应的
        response.xpath              可以直接使用xpath方法来解析页面元素
        response.extract()          提取selector对象的data属性值
        response.extract_first()    提取的seletor列表的第一个数据


Scrapy 是一个用于网络爬虫的 Python 框架，它的工作原理基于组件化设计，各个部分协同工作完成网页爬取任务。其核心工作流程如下：
    引擎（Engine）：作为核心调度器，协调其他所有组件的工作，确保数据在系统中有序流动。
    调度器（Scheduler）：接收引擎传来的请求，按照一定的规则（如优先级、去重）进行排列和管理，决定下一个要爬取的网页。
    下载器（Downloader）：负责从互联网上下载网页内容，将下载的响应（Response）返回给引擎。
    爬虫（Spiders）：
        定义爬取的起始 URL 和爬取规则
        处理下载器返回的响应，提取感兴趣的数据（Item）
        生成新的待爬取 URL 请求，返回给引擎
    项目管道（Item Pipeline）：处理爬虫提取的结构化数据，进行清洗、验证、存储（如保存到数据库、文件）等操作。
    中间件（Middlewares）：
        下载中间件：在请求发送到下载器前或响应返回给爬虫前进行处理（如设置代理、User-Agent）
        爬虫中间件：在引擎和爬虫之间处理请求和响应
工作流程简述：
    1. 爬虫开始时，将初始 URL 生成请求交给引擎
    2. 引擎将请求传给调度器排队
    3. 调度器将请求通过引擎传给下载器
    4. 下载器下载网页内容，生成响应通过引擎传给爬虫
    5. 爬虫处理响应，提取数据（交给管道处理）和新的请求（交给调度器）
    6. 重复上述过程，直到调度器中没有待处理的请求，爬虫结束

进入scrapy shell,直接在终端中输入 scrapy shell 域名
想要看到高亮或自动补全 安装ipython pip install ipython


crawlspider
scrapy genspider -t crawl 项目名 域名