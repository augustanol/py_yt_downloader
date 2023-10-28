import yt_dlp

URLS = ['https://www.youtube.com/watch?v=hHb3owr6PQg']

ydl_opts = {
    'format': 'bestaudio/best',
    'ffmpeg_location': 'C:/ffmpeg/bin',
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
