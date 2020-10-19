#!/usr/bin/env python3

import opml
import feedparser
import youtube_dl
import sys
from glob import glob
from pprint import pprint

if sys.version_info[0] < 3:
    raise Exception('Must be using Python 3')

from time import time, mktime, strptime
from datetime import datetime

if len(glob('last.txt')) == 0:
    f = open('last.txt', 'w')
    f.write(str(time()))
    print('Initialized a last.txt file with current timestamp.\n')
    f.close()

else:
    f = open('last.txt', 'r')
    content = f.read()
    f.close()

    outline = opml.parse('subscription_manager.xml')

    ptime = datetime.utcfromtimestamp(float(content))
    ftime = time()

    urls = []
    for i in range(0,len(outline[0])):
        urls.append(outline[0][i].xmlUrl)

    videos = []
    for i in range(0,len(urls)):
        print('Parsing through channel '+str(i+1)+' out of '+str(len(urls)), end='\r')
        feed = feedparser.parse(urls[i])['items']
        for j in range(0,len(feed)):
            timef = feed[j]['published_parsed']
            dt = datetime.fromtimestamp(mktime(timef))
            if dt > ptime:
                videos.append(feed[j]['link'])

    if len(videos) == 0:
        print('\nSorry, no new video found')
    else:
        print('\n'+str(len(videos))+' new videos found')
        youtube_dl.YoutubeDL({
            'ignoreerrors': True,
            'match_filter': youtube_dl.utils.match_filter_func("!is_live"),
            'subtitleslangs': 'en',
            'writesubtitles': True,
            'outtmpl': 'E:/VODs/Youtube/%(upload_date)s_%(uploader)s_%(title)s.%(ext)s'
        }).download(videos)

    f = open('last.txt', 'w')
    f.write(str(ftime))
    f.close()
