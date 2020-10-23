#!/usr/bin/env python3

# import feedparser
import youtube_dl

# # CONSTANTS
# dl_from = 0
# dl_to = 6
# feed_link = "https://www.youtube.com/feeds/videos.xml?channel_id=UC8b4hCq0aHQbl0v2il0tR_A"

# videos = []
# feed = feedparser.parse(feed_link)['items']
# for i in range(dl_from,dl_to):
#     videos.append(feed[i]['link'])

youtube_dl.YoutubeDL({
    'ignoreerrors': True,
    'match_filter': youtube_dl.utils.match_filter_func("!is_live"),
    'subtitleslangs': ['en'],
    'writesubtitles': True,
    'format': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
    'outtmpl': 'E:/VODs/Youtube/%(upload_date)s_%(uploader)s_%(title)s.%(ext)s'
# }).download(videos)
}).download(["https://www.youtube.com/watch?v=hpjV962DLWs","https://www.youtube.com/watch?v=Ml0qGtY3p5A","https://www.youtube.com/watch?v=MzVKsltzYdI","https://www.youtube.com/watch?v=jRLfGwQ7Nsw","https://www.youtube.com/watch?v=p-yD_16bkIc","https://www.youtube.com/watch?v=lt2Pf9JnYds","https://www.youtube.com/watch?v=mpe1R6veuBw","https://www.youtube.com/watch?v=XQsZNaia3ck","https://www.youtube.com/watch?v=VaqLk1YCv-s","https://www.youtube.com/watch?v=AjejHGuIEro","https://www.youtube.com/watch?v=-k45h6zQs2k","https://www.youtube.com/watch?v=ML3WG_9mN08","https://www.youtube.com/watch?v=41_d4D7T6uI","https://www.youtube.com/watch?v=DM8Tm9ycGz4","https://www.youtube.com/watch?v=ltnEayMzX9c","https://www.youtube.com/watch?v=Twix375Me4Q","https://www.youtube.com/watch?v=whxGyC5GhkI","https://www.youtube.com/watch?v=7T-iX41IFxc","https://www.youtube.com/watch?v=76eeyjzNWcw","https://www.youtube.com/watch?v=FASUZRYs0fM","https://www.youtube.com/watch?v=0gwRG9uForA","https://www.youtube.com/watch?v=OdyZ2CxhMqw","https://www.youtube.com/watch?v=PZbkF-15ObM","https://www.youtube.com/watch?v=l0Md9qwWQBI","https://www.youtube.com/watch?v=-gNlptSlc3k","https://www.youtube.com/watch?v=jtGnnC-hNq8","https://www.youtube.com/watch?v=v6aqDZW1BUM","https://www.youtube.com/watch?v=sjhGAvFJL_I","https://www.youtube.com/watch?v=GgnClrx8N2k","https://www.youtube.com/watch?v=3iZ9JRVmJ5o","https://www.youtube.com/watch?v=kPpV2basTgI","https://www.youtube.com/watch?v=mj-v6zCnEaw","https://www.youtube.com/watch?v=vL2ItIOJyw4","https://www.youtube.com/watch?v=goFY8Q8rnC4","https://www.youtube.com/watch?v=Nr7ZBJtn4QU","https://www.youtube.com/watch?v=oolg6NkWvXI","https://www.youtube.com/watch?v=cGMWL8cOeAU","https://www.youtube.com/watch?v=oiOPEQqfPRQ","https://www.youtube.com/watch?v=GKusxVRxbxo","https://www.youtube.com/watch?v=O93YpTYCWRk","https://www.youtube.com/watch?v=Ri4j8IEG9x4","https://www.youtube.com/watch?v=Wr9ie2J2690","https://www.youtube.com/watch?v=eVyTtWR-sOs","https://www.youtube.com/watch?v=MLAJnv8NkJY","https://www.youtube.com/watch?v=JRo3ayKS2Vc","https://www.youtube.com/watch?v=z5rRZdiu1UE","https://www.youtube.com/watch?v=eBShN8qT4lk","https://www.youtube.com/watch?v=AvlhFPP8vHc","https://www.youtube.com/watch?v=qxDSTCaWVZY","https://www.youtube.com/watch?v=KsPJt7X9r_8","https://www.youtube.com/watch?v=wWGlyVUrwnw","https://www.youtube.com/watch?v=1daMpenuJ7o","https://www.youtube.com/watch?v=7iA-LouDnj4","https://www.youtube.com/watch?v=smuVBQAOvOc","https://www.youtube.com/watch?v=ZzGVOjc3Dig","https://www.youtube.com/watch?v=x7ok5AV7ZrM","https://www.youtube.com/watch?v=ncrqZkyZPbk","https://www.youtube.com/watch?v=9u_v9H24PfY","https://www.youtube.com/watch?v=qiG064009Yc","https://www.youtube.com/watch?v=aJoo79OwZEI","https://www.youtube.com/watch?v=v4xZUr0BEfE","https://www.youtube.com/watch?v=O0lf_fE3HwA","https://www.youtube.com/watch?v=u1xrNaTO1bI","https://www.youtube.com/watch?v=PI_Jl5WFQkA","https://www.youtube.com/watch?v=JQfLSkMK36c","https://www.youtube.com/watch?v=A7fuuDc2hH0","https://www.youtube.com/watch?v=_AjJpSV0I4M","https://www.youtube.com/watch?v=H-tqpHETYhc","https://www.youtube.com/watch?v=icPhDK3PTqc","https://www.youtube.com/watch?v=jVxffY_Gpso","https://www.youtube.com/watch?v=NPcXk0kcqng","https://www.youtube.com/watch?v=ducbn5nUmUs","https://www.youtube.com/watch?v=ATb7CXX-Kc0","https://www.youtube.com/watch?v=7Dj6dVserfw","https://www.youtube.com/watch?v=BHfE682mm3c","https://www.youtube.com/watch?v=ZufwRWceXlc","https://www.youtube.com/watch?v=wZqNUo6y52Q","https://www.youtube.com/watch?v=yQ0iTDafXuM","https://www.youtube.com/watch?v=O4Lsah7bEJY","https://www.youtube.com/watch?v=oJoXOHyerGE"])
