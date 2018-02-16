# 批量下载这个网页上日本妹子的图片
# http://tieba.baidu.com/p/2166231880

import re
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
dir = 'E:\AllPrj\PyCharmPrj\py-crawler\爬取这个日本妹子的图片\Imgs\\'

def get_jpg_urls(url):
    res = requests.get(url, headers=headers)
    urls = re.findall('<img pic_type="0" class="BDE_Image" src="(.*?)"', res.text)
    download_jpg(urls)

def download_jpg(urls):
    global file
    for i, url in enumerate(urls):
        print(i, url)
        # 每张图片打开一次文件，用二进制形式打开
        file = open(dir+str(i)+'.jpg', 'wb')
        jpg = requests.get(url, headers=headers)
        # content对象不是很了解
        file.write(jpg.content)
        file.close()

def main():
    global file
    get_jpg_urls('http://tieba.baidu.com/p/2166231880')

if __name__ == '__main__':
    main()
