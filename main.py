#!/usr/bin/python3
from pytube import YouTube
link = input("Enter the link you want to fetch: ")
yt = YouTube(link)
#details

print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length of the video: ", yt.length)
print("Description: ",yt.description)
print("Ratings: ",yt.rating)
print("Available Streams: ", yt.streams.filter(only_video = True))

#filtering progressive streams
yt.streams.filter(progressive = True)

#getting highest resolution
ys = yt.streams.get_highest_resolution()


print("Downloading...")

ys.download()
print("Download completed")