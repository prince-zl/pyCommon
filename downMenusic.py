import requests
from lxml import etree
import os
import stat
import urllib.request
import sys

fileDownList = [{'url': "http://www.zhengjian.org/taxonomy/term/10875", 'save': "D:/天音/歌曲/男生独唱"},
                {'url': 'http://www.zhengjian.org/taxonomy/term/10874',
                    'save': "D:/天音/歌曲/女生独唱"},
                {'url': 'http://www.zhengjian.org/taxonomy/term/10871',
                    'save': "D:/天音/歌曲/小合唱"},
                {'url': 'http://www.zhengjian.org/taxonomy/term/10872',
                    'save': "D:/天音/歌曲/其他"},  # 11
                {'url': 'http://www.zhengjian.org/taxonomy/term/10873',
                    'save': "D:/天音/歌曲/儿歌"},  # 11
                # //
                {'url': 'http://www.zhengjian.org/taxonomy/term/10876',
                    'save': "D:/天音/歌曲/重唱"},
                {'url': 'http://www.zhengjian.org/taxonomy/term/11256',
                    'save': "D:/天音/歌曲/大合唱"},
                {'url': 'http://www.zhengjian.org/taxonomy/term/10834',
                    'save': "D:/天音/乐曲/民族乐曲"},
                {'url': 'http://www.zhengjian.org/taxonomy/term/10835',
                    'save': "D:/天音/乐曲/西洋乐曲"},
                {'url': 'http://www.zhengjian.org/taxonomy/term/10881',
                    'save': "D:/天音/乐曲/伴奏音乐"},
                ]

# print('请选择：')

# print('请输入:'+str(index)+'----'+fileDownList[index]['save'])
# num = int(input('请输入0-'+str(len(fileDownList)-1)+':进行下载'))
print('启动自动下载程序开始下载')

# print(num)
num = 0


def progressbar(cur, total=100):
    percent = '{:.2%}'.format(cur / total)
    sys.stdout.write('\r')
    # sys.stdout.write("[%-50s] %s" % ('=' * int(math.floor(cur * 50 / total)),percent))
    sys.stdout.write("[%-100s] %s" % ('=' * int(cur), percent))
    sys.stdout.flush()


def schedule(blocknum, blocksize, totalsize):
    if totalsize == 0:
        percent = 0
    else:
        percent = blocknum * blocksize / totalsize
    if percent > 1.0:
        percent = 1.0
    percent = percent * 100
    print("download : %.2f%%" % (percent))
    progressbar(percent)


class New():
    def __init__(self):
        self.url = ''
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        # self.getList(self.url)

    # 获取作者
    def getAuthor(self, url):
        self.url = fileDownList[num]['url']
        res = self.commonGet(url)
        items = res.xpath(
            '//ul[@class="zj-tax-list"]//li')
        for item in items:
            title = item.xpath('.//span//a/text()')[0].strip()
            link = 'http://www.zhengjian.org' + \
                item.xpath('.//span//a/@href')[0]
            print(url, link, title)
            self.getList(link, title)

        next_url = res.xpath(
            '//li[@class="pager__item pager__item--next"]//a/@href')
        print("获取下一页")
        print(next_url)
        if next_url:
            print('开始弄')
            urls = self.url + next_url[0]
            print(urls)
            self.getAuthor(urls)
            print('下一页')
            print(next_url)

    def getList(self, url, title):
        response = self.commonGet(url)
        url = response.xpath(
            '//div[@class="field--item"]//audio//source/@src')
        if url:
            urls = 'http://www.zhengjian.org' + url[0]
            self.downFile(title, urls)

    def downFile(self, title, url):
        print(fileDownList[num]['save'])
        file_path = fileDownList[num]['save']
        # 是否有这个路径
        if not os.path.exists(file_path):
            # 创建路径
            os.makedirs(file_path)
        file_suffix = os.path.splitext(url)[1]
        filename = '{}{}{}{}'.format(file_path, os.sep, title, file_suffix)
        # print('文件名：'+filename)
        # print('下载地址：'+url)
        if not os.path.exists(title):
            try:
                opener = urllib.request.build_opener()
                opener.addheaders = [
                    ('User-Agent', self.headers['User-Agent'])]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(url, filename, schedule)
                print('下载完成_'+filename)
            except Exception as e:
                print('异常')
                print(e)

    def commonGet(self, url):
        res = requests.get(url, headers=self.headers)
        res.encoding = "utf8"
        response = etree.HTML(res.text)
        return response


for idx in range(len(fileDownList)):
    num = idx
    url = fileDownList[idx]['url']+'?page=0'
    new = New()
    new.getAuthor(url)
