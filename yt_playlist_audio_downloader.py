# https://docs.python.org/pt-br/3.13/library/tkinter.html
# https://pytubefix.readthedocs.io/en/latest/user/install.html

from pytubefix import Playlist  # type:ignore
import tkinter
from tkinter import filedialog

# p = Playlist(
#     "https://www.youtube.com/
# watch?v=SNE2oCZH_4k&list=PLT_n1uDi6y9A3UbiU08QYZLjX4PJMQUm1")


def download_audio(playlist: Playlist, path):
    print(f"{playlist.title} {len(playlist.videos)} audios to download")
    for index, video in enumerate(playlist.videos):
        try:
            ys = video.streams.get_audio_only()
            ys.download(output_path=path)
            print(f'Audio {index+1} download complete')
        except Exception as e:
            print(e)


def file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"folder:{folder}")
    return folder


root = tkinter.Tk()
root.withdraw()
url = input("Enter a Youtube playlist url: ")
playlist = Playlist(url)
save_folder = file_dialog()
if save_folder:
    download_audio(playlist=playlist, path=save_folder)
else:
    print('choose a save location')
