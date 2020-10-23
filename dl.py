#!/usr/bin/env python3

import youtube_dl
import sys

from feedparser import parse as feed_parse
from opml import parse as opml_parse

from readchar import readchar
from glob import glob
from pprint import pprint
from time import time, mktime
from datetime import datetime


# Gets 'y' or 'n' response to a query without waiting for 'enter' keypress
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

# Exits program with optional message, either without waiting or with waiting for only a single keypress
def peace_out(message, wait=True, code=0):
    print(message)
    if wait:
        print('Press any key to exit.', end='')
        sys.stdout.flush()
        readchar()
    sys.exit(code)

# Main
def main():
    # If no last-run timestamp, assume this is the first run and only create one
    if len(glob('last.txt')) == 0:
        f = open('last.txt', 'w')
        f.write(str(time()))
        print('Initialized a last.txt file with current timestamp.\n')
        f.close()
        peace_out("First run successful.")

    # Get timestamp from 'last.txt'
    f = open('last.txt', 'r')
    content = f.read()
    f.close()

    # Create list of channels to search through
    urls = opml_parse('subscription_manager.xml')[0]

    # Parse last-run time and set current-run time
    ptime = datetime.utcfromtimestamp(float(content))
    ftime = time()

    # Search through channel list to find any videos published after last-run time
    videos = []
    for i in range(0,len(urls)):
        feed = feed_parse(urls[i].xmlUrl)['items']
        print('Parsing through channel '+str(i+1)+' out of '+str(len(urls)))
        for j in range(0,len(feed)):
            timef = feed[j]['published_parsed']
            dt = datetime.fromtimestamp(mktime(timef))
            print
            if dt > ptime:
                print(f'New video by {feed[j]["author"]}: {feed[j]["title"]}')
                videos.append(feed[j])

    if len(videos) == 0: peace_out('\nNo new videos.')
    videos.sort(key = lambda vid: vid['published'])

    # Query for whether to download each new video found
    videos_requested = []
    print(f'\n{str(len(videos))} new videos')
    for i in range(0,len(videos)):
        if get_y_n(f'\nVideo {i+1}, published {videos[i]["published"]} by {videos[i]["author"]}: {videos[i]["title"]}\nDownload (y/n)? '):
            videos_requested.append(videos[i])

    if len(videos_requested) == 0: peace_out('\nNo more videos to download.')

    # Download each requested video
    for vid in videos_requested:
        try:
            print(f'\n*** Downloading video published {vid["published"]} by {vid["author"]}: {vid["title"]} ***')
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

    # Set last-run time to current-time
    f = open('last.txt', 'w')
    f.write(str(ftime))
    f.close()

    peace_out('\nDownloads complete.')

# Main
if __name__ == "__main__":
    if sys.version_info[0] < 3: peace_out('Must be using Python 3.', False, 1)
    try: main()
    except KeyboardInterrupt: peace_out('Exiting.', False)
