# Code based on Python 3.x
# _*_ coding: utf-8 _*_
# __Author: "LEMON"


from bs4 import BeautifulSoup
import requests
import csv


def download(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    req = requests.get(url, headers=headers)
    return req.text


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    body = soup.body
    data_main = body.find('div', {'class': 'newlist_list_content'})
    tables = data_main.find_all('table')

    zw_list = []
    for i,table in enumerate(tables):
        if i == 0:
            continue
        temp = []
        tds = table.find('tr').find_all('td')
        zwmc = tds[0].find('a').get_text()
        zw_link = tds[0].find('a').get('href')
        fkl = tds[1].find('span').get_text()
        gsmc = tds[2].find('a').get_text()
        zwyx = tds[3].get_text()
        gzdd = tds[4].get_text()
        gbsj = tds[5].find('span').get_text()

        tr_brief = table.find('tr', {'class': 'newlist_tr_detail'})
        brief = tr_brief.find('li', {'class': 'newlist_deatil_last'}).get_text()

        temp.append(zwmc)
        temp.append(fkl)
        temp.append(gsmc)
        temp.append(zwyx)
        temp.append(gzdd)
        temp.append(gbsj)
        temp.append(brief)
        temp.append(zw_link)

        zw_list.append(temp)
    return zw_list


def write_data(data, name):
    filename = name
    with open(filename, 'a', newline='', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)

if __name__ == '__main__':

    basic_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&sm=0&p='

    number_list = list(range(90)) # total number of page is 90
    for number in number_list:
        num = number + 1
        url = basic_url + str(num)
        filename = 'zhilian_DA.csv'
        html = download(url)
        # print(html)
        data = get_content(html)
        # print(data)
        print('start saving page:', num)
        write_data(data, filename)
