requirements = []
import time
import os
try:
    from pytube import YouTube
except:
    requirements.append("pytube")

if requirements != []:
    print(f"You need to install the following packages with pip:", *requirements)
    print("\ntab will close in 10s")
    time.sleep(10)
    exit()

videos = []

try:
    open(f"{os.path.dirname(os.path.abspath(__file__))}\\presenceCheck","x")
    os.mkdir(f"{os.path.dirname(os.path.abspath(__file__))}\\videos")
    print("First time Setup complete.\n\n--------------------------------------------\n")
except:
    pass


print("Enter YouTube links (e.g. https://www.youtube.com/watch?v=dQw4w9WgXcQ) *Leave empty if you've listed all the videos you want to download.*")
while True:
    try:
        video = input(" - ")
        if "/" not in video:
            break
    except Exception as e:
        break
    videos.append(video)
print("Starting to download...")


for song in videos:
    try:
        video_url = song
        video = YouTube(video_url, use_oauth=True, allow_oauth_cache=True)
        video.streams.filter(res="720p",mime_type="video/mp4").first().download(f"{os.path.dirname(os.path.abspath(__file__))}\\videos") 
        print(f"    - DOWNLOADED {song}")
    except Exception as error:
        print(f"{error} *ERROR WITH {song}*")
print("\n--------------------------------------------\n\n*DONE DOWNLOADING*")
print("tab will close in 10s")
time.sleep(10)
