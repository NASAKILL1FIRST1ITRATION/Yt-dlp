#!/usr/bin/env python
import os
from yt_dlp import YoutubeDL
def yotube_to_mp4 (link):
    url = link

    with YoutubeDL() as ydl: 
      info_dict = ydl.extract_info(url, download=True)
      video_url = info_dict.get("url", None)
      video_id = info_dict.get("id", None)
      video_title = info_dict.get('title', None)
      print("Title: " + video_title)

    os.system(f'yt-dlp {url}')

    return [video_url, video_id,video_title]











