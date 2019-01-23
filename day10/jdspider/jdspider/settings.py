# -*- coding: utf-8 -*-

# Scrapy settings for jdspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jdspider'

SPIDER_MODULES = ['jdspider.spiders']
NEWSPIDER_MODULE = 'jdspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jdspider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jdspider.middlewares.JdspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jdspider.middlewares.JdspiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'jdspider.pipelines.JdspiderPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
DEFAULT_REQUEST_HEADERS = {
    'cookie': 'shshshfpa=199f7fac-4ab9-8725-bf62-4d9479dc3a4d-1545285424; _pst=347298771-131709; unick=%E5%87%89%E6%B0%B4u; pin=347298771-131709; _tp=%2BnxllPuZ7mmkCCwPSbW8XqOXmhCdxELGgzo3jt6dBDE%3D; __jdu=1411702269; xtest=3251.cf6b6759; ipLoc-djd=1-72-2799-0; qrsc=3; cn=0; shshshfpb=hvazE1KCoTMDOKAyrr%20EKiA%3D%3D; unpl=V2_ZzNtbUNeQBAhC0UGeBtUUmJXQF9LAkRAIgkVUXxJCQRgAxdaclRCFX0UR1RnGlwUZAIZXUNcQxdFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHscXAVhAhFeRV9zJXI4dmR5GV0AYwMiXHJWc1chVENWcxFbACoDF11CUUIWdg9OZHopXw%3d%3d; __jda=122270672.1411702269.1545285418.1547468310.1548072614.6; __jdc=122270672; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_0824e22c239f4ec38d6df0b46ad06146|1548072613549; user-key=23052098-87a3-43a3-b0c1-943d684cdbe3; PCSYCityID=412; shshshfp=903e2e2417fdbcc864f93b1c9c763092; rkv=V0300; 3AB9D23F7A4B3C9B=ZVW5VL3CKCDFFRUOD7OL2RSFROBL243Z5XGU3UXTBPGABBBN6GB6S6HNXRVCRZ62ROPFF5YSBXFYTMG2HBZUHQCORY; __jdb=122270672.4.1411702269|6.1548072614; shshshsID=a3be6d1cf19ff179cb7e2b4c20935f4c_4_1548072696978',
    'referer': 'https://search.jd.com/search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&uc=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}
