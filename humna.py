# 爬取图片
# 三层爬虫

# 第1层：https://www.uumnt.cc/zt/rentiyishu.html
# 第2层：https://www.uumnt.cc/xinggan/25783_1.html
# 第3层：https://newimg.uumnt.cc:8092/Pics/2018/0218/02/01.jpg



import re
import time
import requests
from bs4 import BeautifulSoup


count = 165

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def get_urls(url):
    res = requests.get(url, headers=headers)
    # 首页主角分类的链接
    links = re.findall('<a href="/xinggan(.*?).html" title=', res.text)[6::]

    # links = ['/25783']

    for link in links:
        print('on page:' + 'https://www.uumnt.cc/xinggan{link}_1.html'.format(link=link))
        maxpage = get_maxpage('https://www.uumnt.cc/xinggan{link}_1.html'.format(link=link))
        imglinks = ['https://www.uumnt.cc/xinggan{link}_{page}.html'.format(link=link,page=page) for page in range(1, maxpage+1)]
        for imglink in imglinks:
            print(imglink)
            print()
            get_imgs(imglink)
            time.sleep(1)

# 获得每个主角的最大页码
def get_maxpage(url):
    res = requests.get(url, headers=headers)
    maxpage = re.findall('下一页</a><a.*? (.*?)\.html">末页', res.text)[0].split('_')[1]
    return int(maxpage)
    # BS 抓到的为空
    # soup = BeautifulSoup(res.text, 'html.parser')
    # return  soup.select('#contbody > div:nth-of-type(7) > div > div.page > a:nth-of-type(7)')

def get_imgs(url):
    global count
    count += 1
    print('第{}张'.format(count))
    res = requests.get(url, headers=headers)
    scrlink = re.findall('<img src="(.*?)"', res.text)
    # 是否为列表
    if isinstance(scrlink, list) == True:
        # 主图的url在最前面，[0] 为了排除页面上小图片的干扰
        scrlink = scrlink[0]
    print(scrlink)
    jpg = requests.get(scrlink, headers=headers)
    file = open('E:\AllPrj\PyCharmPrj\py-crawler\humans-instinct\imgs\{}.jpg'.format(count), 'wb')
    file.write(jpg.content)
    file.close()

def main():
    url = 'https://www.uumnt.cc/zt/rentiyishu.html'
    get_urls(url)

if __name__ == '__main__':
    main()

