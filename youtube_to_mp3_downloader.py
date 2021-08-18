# YouTube to MP3 Downloader by Azer Jabarli
# 8th August, 2021

from pytube import YouTube # Essential library for working with YouTube
import os # Needed to save the downloaded file
import validators # Needed to check if the link is valid

video_link = YouTube(input("Enter video URL: ")) # Get video URL

while True: # Check for the validity of the URL
	if not validators.url(video_link):
		video_link = YouTube(input("Enter video URL: "))
	else:
		break		

audio = video_link.streams.filter(only_audio = True).first() # Extract the audio from the video

file = audio.download(output_path = "C:\\Users\\user\\Music") # Downloading the file to the directory in the argument

base, extension = os.path.splitext(file) # Splitting the file path 
os.rename(file, base + ".mp3") # Saving the file

print("Success!")
input("Press any key to exit...")
