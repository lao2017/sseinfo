# -*- coding: utf-8 -*-

# Scrapy settings for sseinfo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sseinfo'

SPIDER_MODULES = ['sseinfo.spiders']
NEWSPIDER_MODULE = 'sseinfo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sseinfo (+http://www.yourdomain.com)'
USER_AGENT = 'MOZilla/5.0(x11; Linux x86_64; rv:7.0.1)Gecko/20100101 Firefox/7.7'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
COOKIES_ENABLED = False

#下载延迟限制
#DOWNLOAD_DELAY  = 3
#输出日志等级
#LOG_LEVEL = 'DEBUG'
#LOG_LEVEL = 'INFO'
#不加以下设置以json格式打印
LOG_LEVEL = 'ERROR'




# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sseinfo.middlewares.SseinfoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     # 'sseinfo.middlewares.SseinfoDownloaderMiddleware': 543,
#     # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
#     # 'sseinfo.middlewares.MyproxiesSpiderMiddleware':125
#
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':543,
#     'sseinfo.middlewares.ProxyMiddleWare':125,
#     'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':543
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'sseinfo.pipelines.SseinfoPipeline': 300,
}

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
#
# IPPOOL=[
#     {"ipaddr":"112.67.178.234:9797"},
#     {"ipaddr":"123.121.91.216:9000"},
#     {"ipaddr":"121.43.178.58:3128"},
#     {"ipaddr":"125.88.177.128:3128"},
#     {"ipaddr":"182.121.204.78:9999"},
#     {"ipaddr":"119.29.92.171:8888"},
#     {"ipaddr":"183.30.204.159:9999"}
# ]

#FILES_STORE = '/PycharmProjects/sseinfo'
#FILES_STORE = '/data'

#MONGO_URI = '115.159.114.78:29999'

# MONGO_URI = '10.10.13.211:27017'
# MONGO_DATABASE = 'Testsseinfo'

MONGO_URI = 'localhost:27017'
MONGO_DATABASE = 'Test'

