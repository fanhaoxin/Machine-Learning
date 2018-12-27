# 3.6.5

import requests
from lxml import etree
import json

def getOnePage(n):

    # 字符串的格式化
    url = f'https://maoyan.com/board/4?offset={n*10}'
    # url = 'https://maoyan.com/board/4?offset={}'.format(n)
    # url = 'https://maoyan.com/board/4?offset=%d' % n

    # 告诉服务器 我们是浏览器 字典
    header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400'}

    # .调用
    r = requests.get(url, headers=header)

    # # 输出到屏幕 200 http 状态码
    # print(r)

    # # 打印文本
    # print(r.text)

    # 返回文本
    return r.text

def parse(text):
    
    # 初始化 标准化
    html = etree.HTML(text)
    # 提取我们想要的信息 需要些xpath语法
    # names 是列表 xpath返回一定是列表
    names = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')

    print(names)

    releasetimes = html.xpath('//p[@class="releasetime"]/text()')

    print(releasetimes)

    # 字典
    item = {} # dict

    # zip 函数是拉链函数
    for name, releasetime in zip(names, releasetimes):
        # print(name, releasetime)

        item['name'] = name
        item['releasetime'] = releasetime
        # 生成器 循环迭代
        yield item

#保存数据
def save2File(data):
    with open('movie.json', 'a', encoding='utf-8') as f:
        # 把字典 列表 转化成字符串'\n'换行
        data = json.dumps(data, ensure_ascii=False) + ',\n'
        f.write(data)

def run():

    for n in range(0, 10):

        data = getOnePage(n)

        # print(data)

        items = parse(data)

        for item in items:
            print(item)
            save2File(item)

if __name__ == '__main__':
    run()