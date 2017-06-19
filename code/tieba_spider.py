# _*_ coding: utf-8 _*_

import urllib2
#file_name文件路径，text要写进的字符串
def write_file(file_name,text):
    print '正在存储文件'+file_name
    f=open(file_name,'w+')
    f.write(text)
    f.close()

#把爬取页面的过程封装成一个小函数
def load_page(url):
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    html=response.read()
    return html

if __name__=='__main__':
    bdurl=str(raw_input('请输入贴吧的地址，去掉pn=后面的数字:'))
    begin_page=int(raw_input('请输入开始的页数:'))
    end_page=int(raw_input('请输入结束的页数:'))

#写一个百度贴吧爬虫接口
def tieba_spider(url,begin_page,end_page):
    #浏览器代理
    user_agent='Mozilla/5.0(compatible;MSIE 9.0;Windows NT 6.1;Trident/5.0)'
    headers={'User-Agent':user_agent}
    for i in range(begin_page,end_page+1):
        pn=50*(i-1)
        html=load_page(url+str(pn))
        file_name=str(i)+'.html'
        print '正在下载第'+str(i)+'个网页'
        write_file("/home/zhangwc/Applications/git/Scrapy/spider_tieba/data/"+str(i)+".html",html)
        #此处指定位置则报错non-keyword arg after keyword arg，为啥？如何解决？
tieba_spider(bdurl,begin_page,end_page)