import os
from pathlib import Path
import shutil


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
        ".alac", ".amr", ".ape", ".au", ".dss",
        ".flac", ".flv", ".m4a", ".m4b", ".m4p",
        ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
        ".opus", ".qcp", ".tta", ".voc", ".wav",
        ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
        ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
    ".gif", ".webp", ".svg", ".apng", ".avif")

ebooks - ('.tpz', '.lrf', '.tk3', '.aep', '.dnl', '.opf', '.fb2', '.ncx', 
        '.rzs', '.lrs', '.ybk', '.lit', '.rzb', '.ebk', '.han', '.nva', '.mbp', '.prc', '.azw', '.opf', '.ceb', '.cbc', '.kfx', '.lrx', '.phl', '.tcr', '.edn', '.orb', '.oeb', '.ava', '.bkk', '.tr3', '.opz', '.snb', '.etd', '.eal', '.vbk', '.pef', '.qmk', '.fkb', '.pml')

ebook = ()
def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

def 


username = os.getlogin()

os.chdir(f"/Users/{username}/Downloads")

Path("audio").mkdir(exist_ok=True)
Path("video").mkdir(exist_ok=True)
Path("image").mkdir(exist_ok=True)
Path("screenshot").mkdir(exist_ok=True)


for file in os.listdir():
    if is_audio(file):
        shutil.move(file, "/Users/{username}/Downloads/audio")
    elif is_video(file):
        shutil.move(file, "/Users/{username}/Downloads/video")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, "/Users/{username}/Downloads/screenshot")
        else:
            shutil.move(file, "/Users/{username}/Downloads/image")
    else:
        shutil.move(file, "/Users/{username}/Downloads/misc")
