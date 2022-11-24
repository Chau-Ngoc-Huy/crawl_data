from __future__ import unicode_literals
import youtube_dl

youtube_url = [
    'https://www.youtube.com/watch?v=I4Ri10dlYDM',
    'https://www.youtube.com/watch?v=X7V3dBsE5Q4',
]

ydl_opts = {
    "outtmpl": "/home/huycn/Documents/School/Python/data/%(title)s.%(ext)s",
    "ratelimit": 42000000,
    "http_chunk_size": 10485760,
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(youtube_url)
