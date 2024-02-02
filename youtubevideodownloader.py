from pytube import YouTube
a=input("enter link: ")
link=YouTube(a)
print(link.title)
print(link.thumbnail_url)
video=link.streams.get_highest_resolution()
video.download()
print("video downloaded")