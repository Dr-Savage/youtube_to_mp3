import youtube_dl 
import subprocess
def run():
    #link the video i wants to download
    video = input("paste the youtube url:")
    #download and convert into mp3
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video, download = False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format':'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    subprocess.call(["open",filename])

if __name__ == '__main__':
    run()
