from pytube import youtube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_streams = streams.get_highest_resolution()
        highest_res_streams.download(output_path=save_path)
        print("Video downloaded successfully")

    except Exception as e:
        print(e)

url = ""
save_path = "C:\Users\prec1\PycharmProjects\helloworld\pythonProject"

download_video(url, save_path)