import os
import sys
from scrapy.cmdline import execute

# 运行/调试入口
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'jiacom'])
