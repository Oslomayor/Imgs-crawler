# 夏美酱图片
# URL:
# https://www.changshifang.com/zgmt/114390.html
# https://www.changshifang.com/zgmt/114390_2.html
# ...
# https://www.changshifang.com/zgmt/114390_11.html

import os
import requests
import time
from lxml import etree


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}

img_links = []

# 参数为保存路径
def download_img(dir):
    count = 0
    for item in img_links:
        count += 1
        jpg = requests.get(item, headers=headers)
        file = open(dir + '/夏美酱img/夏美酱part1_{}.jpg'.format(count), 'wb')
        file.write(jpg.content)
        file.close()

def main():

    # 获取当前脚本运行路径
    dir = os.getcwd()
    # 创建文件夹
    if False == os.path.exists(dir + '/夏美酱img'):
        os.mkdir(dir + '/夏美酱img')
    else:
        pass

    count = 0

    # range(a,b) 的范围是[a,b), 左闭右开
    urls = ['https://www.changshifang.com/zgmt/114390.html'] \
           + ['https://www.changshifang.com/zgmt/114390_{}.html'.format(page) for page in range(2,13)]

    for url in urls:
        count += 1
        print(url)
        time.sleep(1)
        res = requests.get(url=url, headers=headers)
        selector = etree.HTML(res.text)
        # XPath 语法其实挺简单，img 节点中 src 后的链接，写成 /img/@src
        if count < 4:
            infos = selector.xpath('/html/body/div[5]/div/div[1]/p[1]/a')
        else :
            infos = selector.xpath('/html/body/div[5]/div/div[1]/a')
        # 太坑了，前后的网页的xml构造不一样
        # 前3页
        # /html/body/div[5]/div/div[1]/a[1]/img
        # 后面的
        # /html/body/div[5]/div/div[1]/p[1]/a[2]/img

        for info in infos:
            img_link = 'https://www.changshifang.com' + info.xpath('img/@src')[0]
            img_links.append(img_link)
    download_img(dir)

if __name__ == '__main__':
    main()

