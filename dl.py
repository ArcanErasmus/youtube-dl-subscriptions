#!/usr/bin/env python3

import opml
import feedparser
import youtube_dl
import sys
from readchar import readchar
from glob import glob
from pprint import pprint
from time import time, mktime, strptime
from datetime import datetime

def get_y_n(message):
    out = None
    while out == None:
        print(message, end='')
        sys.stdout.flush()
        response = readchar().decode("utf-8").lower()
        print(response)
        if response.lower() == 'y': out = True
        elif response.lower() == 'n': out = False
    return out

def peace_out(message, wait=True, code=0):
    print(message)
    if wait:
        print('Press any key to exit.', end='')
        sys.stdout.flush()
        readchar()
    sys.exit(code)

def main():
    if len(glob('last.txt')) == 0:
        f = open('last.txt', 'w')
        f.write(str(time()))
        print('Initialized a last.txt file with current timestamp.\n')
        f.close()
        peace_out("First run successful.")

    f = open('last.txt', 'r')
    content = f.read()
    f.close()

    urls = opml.parse('subscription_manager.xml')[0]
    ptime = datetime.utcfromtimestamp(float(content))
    ftime = time()

    videos = []
    for i in range(0,len(urls)):
        feed = feedparser.parse(urls[i].xmlUrl)['items']
        print('Parsing through channel '+str(i+1)+' out of '+str(len(urls)))
        for j in range(0,len(feed)):
            timef = feed[j]['published_parsed']
            dt = datetime.fromtimestamp(mktime(timef))
            print
            if dt > ptime:
                print(f'New video: {feed[j]["title"]}')
                videos.append(feed[j])

    if len(videos) == 0: peace_out('\nNo new videos.')

    videos_requested = []
    print(f'\n{str(len(videos))} new videos')
    # query to download each video
    for i in range(0,len(videos)):
        if get_y_n(f'\nVideo {i+1}, published {videos[i]["published"]}: {videos[i]["title"]}\nDownload (y/n)? '):
            videos_requested.append(videos[i])
        # answer = input(f'\nVideo {i+1}, published {videos[i]["published"]}: {videos[i]["title"]}\nDownload (y/n)? ')
        # if (answer.strip().lower()[0] == 'y'):
            

    if len(videos_requested) == 0: peace_out('\nNo more videos to download.')

    videos_requested.sort(key = lambda vid: vid['published'])
    for vid in videos_requested:
        try:
            youtube_dl.YoutubeDL({
                'ignoreerrors': True,
                'match_filter': youtube_dl.utils.match_filter_func("!is_live"),
                'subtitleslangs': ['en'],
                'writesubtitles': True,
                'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
                'outtmpl': 'E:/VODs/Youtube/%(upload_date)s_%(uploader)s_%(title)s.%(ext)s'
            }).download([vid['link']])
        except KeyboardInterrupt:
            print ('skipping video')

    f = open('last.txt', 'w')
    f.write(str(ftime))
    f.close()

    peace_out('\nDownloads complete.')

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        raise Exception('Must be using Python 3')
    try: main()
    except KeyboardInterrupt: peace_out('Exiting.', False)
