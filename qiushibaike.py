import requests
from bs4 import BeautifulSoup
import bs4
import re

def getHTMLText(url):
    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        r = requests.get(url,headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivlist(lis,li,html,count):
    soup = BeautifulSoup(html,"html.parser")
    try:
        a = soup.find_all('div', attrs={'class': 'content'})
        ll = soup.find_all('div', attrs={'class': 'author clearfix'})
        for sp in a:
            patten = re.compile(r'<span>(.*?)</span>',re.S)
            Info = re.findall(patten,str(sp))
            lis.append(Info)
            count = count + 1
        for mc in ll:
            namePatten = re.compile(r'<h2>(.*?)</h2>', re.S)
            d = re.findall(namePatten, str(mc))
            li.append(d)
    except:
        return ""
    return count

def printUnivlist(lis,li,count):
    for i in range(count):
        a = li[i][0]
        b = lis[i][0]
        print ("%s:"%a+"%s"%b)

def input_enter():
    input1 = input()
    if input1 == 'Q':
        return False
    else:
        return True


def main():
    passage = 0
    enable = True
    for i in range(20):
        mc = input_enter()
        if mc==True:
            lit = []
            li = []
            count = 0
            passage = passage + 1
            qbpassage = passage
            print(qbpassage)
            url = 'http://www.qiushibaike.com/8hr/page/' + str(qbpassage) + '/?s=4966318'
            a = getHTMLText(url)
            fillUnivlist(lit, li, a, count)
            number = fillUnivlist(lit, li, a, count)
            printUnivlist(lit, li, number)
        else:
            break

main()
