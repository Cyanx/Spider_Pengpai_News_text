"""
    @author: Cyan Xin
    @date: 2019/11/29
    @content: The spider of Pengpai News
"""


import time
import csv
import random
import requests
from bs4 import BeautifulSoup


"""
#######################################################
#  获取对应文章的类别，标题，作者，发布时间，文章内容
###########################################################
"""

with open('currentEvents.csv', 'a', encoding='utf-8') as f:
    for a in range(11, 26):
        print('crawling No.' + str(a) + " page")
        # 爬取 25 页(按照这种方式只有25页能够获取到)
        # 可替换 js 爬取不同类别新闻
        # 中国政库
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25462&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15749' + str(random.randint(10000000, 88888888))
        # 中南场
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25488&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15740' + str(random.randint(10000000, 88888888))
        # 舆论场
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25489&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15748' + str(random.randint(10000000, 88888888))
        # 打虎记
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25490&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15747' + str(random.randint(10000000, 88888888))
        # 人事风向
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25423&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15746' + str(random.randint(10000000, 88888888))
        # 法治中国
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25426&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15747' + str(random.randint(10000000, 88888888))
        # 一号专案
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25424&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15748' + str(random.randint(10000000, 88888888))
        # 港台来信
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25463&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15749' + str(random.randint(10000000, 88888888))
        # 长三角政商
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25491&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15748' + str(random.randint(10000000, 88888888))
        # 直击现场
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25428&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15749' + str(random.randint(10000000, 88888888))
        # 公益湃
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=68750&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15739' + str(random.randint(10000000, 88888888))
        # 暖闻
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=27604&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15683' + str(random.randint(10000000, 88888888))
        # 澎湃质量报告
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25464&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15745' + str(random.randint(10000000, 88888888))
        # 绿政公署
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25425&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15749' + str(random.randint(10000000, 88888888))
        # 澎湃国际
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25429&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15749' + str(random.randint(10000000, 88888888))
        # 外交学人
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25481&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15731' + str(random.randint(10000000, 88888888))
        # 澎湃防务
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25430&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15744' + str(random.randint(10000000, 88888888))
        # 唐人街
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25678&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15728' + str(random.randint(10000000, 88888888))
        # 澎湃人物
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25427&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15671' + str(random.randint(10000000, 88888888))
        # 浦江头条
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25422&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15749' + str(random.randint(10000000, 88888888))
        # 教育家
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25487&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15748' + str(random.randint(10000000, 88888888))
        # 全景现场
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25634&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15657' + str(random.randint(10000000, 88888888))
        # 美数课
        # url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25635&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15709' + str(random.randint(10000000, 88888888))
        # 快看
        url_visit = 'https://www.thepaper.cn/load_index.jsp?nodeids=25600&topCids=&pageidx=' + str(a) +'&isList=true&lastTime=15739' + str(random.randint(10000000, 88888888))

        print(url_visit)
        res = requests.get(url_visit)
        res.encoding = 'utf-8'
        # print(res.text)
        soup = BeautifulSoup(res.text, 'lxml')
        # print(soup)
        time.sleep(2)

        link_list = []
        url_head = 'https://www.thepaper.cn/'

        for link in soup.select('.news_li h2 a'):  # 跟上面的方法等价
            # print(link)
            link_list.append(url_head + link.get('href'))
        # print(link_list)

        for item in link_list:
            news = []
            visit = requests.get(item)
            visit.encoding = 'utf-8'
            soup = BeautifulSoup(visit.text, 'lxml')
            # 类别，标题，作者，发布时间，文章内容
            classification = soup.select('body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > div.news_path > a:nth-child(2)')[0].text
            news.append(classification)
            # print(classification)
            title = soup.select('body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > h1')[0].text
            news.append(title)
            # print(title)
            author = soup.select('body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > div.news_about > p:nth-child(1)')[0].text
            news.append(author)
            # print(author)
            release_time = soup.select('body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > div.news_about > p:nth-child(2)')[0].text
            release_time = release_time.strip()
            release_time = release_time[0:16]
            # print(release_time)
            # content = []
            for para in soup.select('body > div.bdwd.main.clearfix > div.main_lt > div.newscontent > div.news_txt'):
                # print(para.text)
                content = para.text
            news.append(content)
            # print(news)
            # 将新闻写入csv文件
            # f.write(codecs.BOM_UTF8)
            writer = csv.writer(f, lineterminator='\n')
            # 它需要一个序列（例如：列表或元组）你给它一个字符串。一个字符串也是一个字符串序列，但它是一个1字符的字符串序列，这不是你想要的。
            # 如果只想要一个字符串您可以这样做：
            # csvwriter.writerow（[JD]） 这会用一个列表包装JD（一个字符串）
            writer.writerows([news])
        # print(len(link_list))
