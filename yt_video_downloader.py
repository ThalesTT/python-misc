# https://docs.python.org/pt-br/3.13/library/tkinter.html
# https://pytubefix.readthedocs.io/en/latest/user/install.html

from pytubefix import YouTube  # type:ignore
from pytubefix.cli import on_progress  # type:ignore
import tkinter
from tkinter import filedialog


def download_video(url, path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        resolution_stream = streams.get_highest_resolution()
        resolution_stream.download(output_path=path)
        print('Video download complete ')
    except Exception as e:
        print(e)


def file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"folder:{folder}")
    return folder


root = tkinter.Tk()
root.withdraw()
url = input("Enter a Youtube url: ")
save_folder = file_dialog()
if save_folder:
    print("downloading... ")
    download_video(url=url, path=save_folder)
else:
    print('choose a save location')
