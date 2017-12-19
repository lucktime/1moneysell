# _*_ coding:utf-8 _*_
# intend:实现小米的1元抢购功能

# step:
# url: http://hd.mi.com/y/08011d/index.html
__author__ = 'lucky'
__version__ = '1.0'
"""
获取的网站页面
    点击抢购按钮时，发生的操作页面
小米账号管理
    账号登录
    账号退出
选择抢购
    如果抢购成功就加入购物车，并且发送微信提醒。
    抢购可能需要输入验证码
"""

"""
抓包类，完成网页抓取的日常操作

"""
# 网络请求
import requests
# 填充表单，设置cookile，模拟浏览器登录
import mechanize
# 页面解析
from bs4 import BeautifulSoup
class PageSpider(object):

    def __init__(self,url):
        self.url = url
        self.br = mechanize.Browser()
        # pass


    # 抢购功能
    """
    step1: 根据url，解析页面。
    step2：找到抢购页面的布局部分。
    step3：判断抢购商品，是否符合抢购要求
    step4：抢购，加入购物车
    step5：判断是否登录
    """
    def flashsale(self):
        content = self.__getcontent()
        print(content)
        # pass
    
    # 私有方法
    """
    根据url 链接，获取链接内容，并且返回解析后的结果。
    """
    def __getcontent(self):
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        try:
            response = self.br.open(self.url)
        except BaseException:
            pass
        html = response.read()
        s = BeautifulSoup(html,"html5lib")  
        return s


class Login(object):
    pass

class NoticeMsg(object):
    pass

def main():
    url = 'http://dailongnet.com/'
    # 初始化抓包类
    spider = PageSpider(url)
    # 实现抢购功能
    spider.flashsale()

if __name__ == '__main__':
    main()
