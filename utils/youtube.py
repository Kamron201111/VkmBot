from youtube_search_python import VideosSearch

def search_youtube(query):
    v = VideosSearch(query, limit=1).result()['result'][0]
    return {"title": v['title'], "url": v['link']}

def download_audio(url):
    out = 'music.mp3'
    ydl = {'format': 'bestaudio', 'outtmpl': out}
    with yt_dlp.YoutubeDL(ydl) as y:
        y.download([url])
    return out
