# coding:utf-8
import urllib2

import re
import BeautifulSoup

# testUrl = 'https://www.lagou.com/'
testUrl = 'http://example.webscraping.com/'


def download(url, user_agent="wswp", num_retyies=2):
    # 设置用户代理
    headers = {"User-agent": user_agent}
    request = urllib2.Request(url, headers=headers)
    # 捕获异常
    try:
        html = urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print "DownLoadError:", e.reason
        html = None
        # 设置重试下载次数
        if num_retyies > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # 错误代码为500到600时，重试2次（默认设置2次）--递归
                return down(url, user_agent, num_retyies - 1)
    return html

# 网站地图
def crawl_siteamp(url):
    sitemap=download(url)
    links=re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html=download(link)
        print html

if __name__ == '__main__':
    # print download(testUrl)
    crawl_siteamp(testUrl)