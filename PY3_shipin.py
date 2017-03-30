#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys
import urllib.request
import requests
import re
import json

# http://www.ximalaya.com/25701225/album/396158


class XimalayaDt:
    def __init__(self, pageurl):
        self._pageurl = pageurl
        self._sidre = re.compile(r'sound_id="(\d+)"')

    def detect(self):
        sids = self._obtainsids()
        line = 'Detect {0} sounds at {1}'.format(len(sids), self._pageurl)
        print(line)
        if len(line) == 0:
            return None

        addrs = self._obtainsaddrs(sids)
        if len(addrs) == 0:
            return None

        self._obtainss(addrs)

    def _obtainsids(self):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            }
        ws = requests.get(self._pageurl, headers=headers).text

        sids = list()
        sml = self._sidre.findall(ws)
        for sid in sml:
            if sid not in sids:
                sids.append(sid)
        return sids

    @staticmethod
    def _obtainsaddrs(sids):
        addrs = list()

        for sid in sids:
            url = 'http://www.ximalaya.com/tracks/{0}.json'.format(sid)

            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            }
            ws = requests.get(url, headers=headers).text
            dicts = json.loads(ws, 'utf-8')

            path = dicts['play_path']
            duration = dicts['duration']
            name = dicts['title']

            addrs.append((name, duration, path))

        return addrs

    def _obtainss(self, addrs):
        index = 0
        for pairs in addrs:
            index += 1
            filepath = pairs[0].strip() + '.' + pairs[2].split('.')[-1]
            print('({0} of {1})   {2}'.format(index, len(addrs), filepath))

            urllib.request.urlretrieve(pairs[2], filepath, self._cbk)

    @staticmethod
    def _cbk(a, b, c):
        per = 100.0 * a * b / c
        if per > 100:
            per = 100

        s = "downloading...{0:.2f}%".format(per)
        print(s, end='\r')


def begin():
    url = input('ENTER PAGEURL, Album or Sound: ')
    url = url.lower().strip()

    if url == '':
        url = 'http://www.ximalaya.com/explore/'

    if 'www.ximalaya.com' not in url:
        print('Invalid url')
        return None

    if not url.startswith('http://'):
        url = 'http://' + url

    XimalayaDt(url).detect()

if __name__ == '__main__':
    os.chdir(sys.path[0])
    begin()
 
