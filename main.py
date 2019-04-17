from scrapy.cmdline import execute
import sys
import os

print(os.path.abspath(__file__))  # 获取main.py的路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 通过main获取父路径即项目路径
execute(["scrapy", "crawl", "bole"])  # 执行scrapy脚本