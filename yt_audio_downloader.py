# https://docs.python.org/pt-br/3.13/library/tkinter.html
# https://pytubefix.readthedocs.io/en/latest/user/install.html

from pytubefix import YouTube  # type:ignore
from pytubefix.cli import on_progress  # type:ignore
import tkinter
from tkinter import filedialog


def download_audio(url, path):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()
        ys.download(output_path=path)
        print('Audio download complete ')
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
    download_audio(url=url, path=save_folder)
else:
    print('choose a save location')
