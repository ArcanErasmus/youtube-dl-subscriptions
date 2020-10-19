#!/usr/bin/env python3

import feedparser
import youtube_dl

# CONSTANTS
dl_from = 0
dl_to = 6
feed_link = "https://www.youtube.com/feeds/videos.xml?channel_id=UC8b4hCq0aHQbl0v2il0tR_A"

videos = []
feed = feedparser.parse(feed_link)['items']
for i in range(dl_from,dl_to):
    videos.append(feed[i]['link'])

youtube_dl.YoutubeDL({
    'ignoreerrors': True,
    'match_filter': youtube_dl.utils.match_filter_func("!is_live"),
    'subtitleslangs': 'en',
    'writesubtitles': True,
    'outtmpl': 'E:/VODs/Youtube/%(upload_date)s_%(uploader)s_%(title)s.%(ext)s'
}).download(videos)
