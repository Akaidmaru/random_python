import os
from pathlib import Path
import shutil   # Operations on files and collection of files


# get the Username of the current user in the system
username = os.getlogin() 

# changes the directory to the working directory
os.chdir(f"/Users/{username}/Downloads")

# audio extension list
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff", ".alac", ".amr", ".ape", 
        ".au", ".dss", ".flac", ".flv", ".m4a", ".m4b", ".m4p", ".mp3", 
        ".mpga", ".ogg", ".oga", ".mogg", ".opus", ".qcp", ".tta", ".voc", 
        ".wav", ".wma", ".wv")

# video extension list
video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
        ".mp4", ".m4p", ".m4v", ".mxf")

# image extension list
img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
        ".gif", ".webp", ".svg", ".apng", ".avif")

# ebook extension list
ebook = (".txt", ".epub", ".mobi", ".azw", ".azw3", ".pdf")

# executable extension list
exe = (".exe", ".bat", ".com", ".cmd", ".inf", ".ipa", ".osx",
        ".pif", ".run", ".wsh", ".msi")

# office extension list
office = (".xls", ".xlsx", ".doc", ".docx", ".ppt", ".pptx", ".ods",
        ".xlt", ".csv", ".odt", ".db", ".dotx", ".odf", ".odp")

# compression extension list
zipped = (".apz", ".b6z", ".sy_", ".zst", ".rte", ".rar", ".pup", ".cit",
        "bz2", ".sfg", ".s00", ".npk", ".deb", ".pkg", ".tbz", ".sit", ".pwa",
        ".dar", ".lzm", ".ice", ".qda", ".sqx", ".ita", ".cbt", ".xip", ".ecs",
        ".dl_", ".gza", ".zpi", ".pit", ".cb7", ".p7z", ".ctx", ".hbe", ".par",
        ".cbr", ".vip", ".uha", ".r00", ".opk", ".zip", ".f3z", ".rev", ".taz",
        ".kgb", ".epi", ".cbz", ".pak", ".sfx", ".nex", ".a02", ".pcv", ".z03",
        ".rpm", ".cdz", ".c00", ".s7z", ".hki", ".tx_", ".ari", ".lz4", ".zix",
        ".whl", ".apk", ".ark", ".tgs", ".ayt", ".sfs", ".a01", ".ipk", ".c10",
        ".spd", ".gmz", ".ace", ".arc", ".r01", ".piz", ".z00", ".spa", ".pea",
        ".cba", ".war", ".fdp", ".sdc", ".snb", ".s02", ".r03", ".ctz", ".ubz",
        ".oar", ".pkz", ".gca", ".p19", ".a00", ".r30", ".mzp", ".c01", ".tgz",
        ".alz", ".rnc", ".rss", ".s01", ".vpk", ".jex", ".spt", ".pup", ".car",
        ".arj", ".xar", ".lzh", ".fp8", ".jhh", ".000", ".jgz", ".z04", ".rp9",
        ".lbr", ".zoo", ".shr", ".pet", ".sar", ".xez", ".tcx", ".lha", ".sea",
        ".hyp", ".pax", ".dgc", ".spl", ".spm", ".psz", ".shk", ".mzp", ".r04",
        ".mbz", ".ain", ".zap", ".xef", ".hbc", ".lqr", ".bza", ".pbi", ".ize",
        ".isx", ".z02", ".xoj", ".lzr", ".edz", ".wdz", ".gzi", ".gz2", ".vib",
        ".cpt", ".nar", ".txz", ".egg", ".ipg", ".z01", ".wux", ".b64", ".zi_",
        ".vsi", ".c02", ".hpk", ".sdn", ".ish", ".tlz", ".prs", ".uc2", ".xzm",
        ".lzo", ".mou", ".arh", ".mar", ".daf", ".stg", ".vwi", ".snz", ".zim",
        ".puz", ".jic", ".yz1", ".pae", ".r02", ".pim", ".wot", ".gar", ".trs",
        ".lzx", ".r21", ".p01", ".wlb", ".efw", ".sen", ".vms", ".pxl", ".ana",
        ".sqf", ".fcx", ".sfm", ".s09", ".cp9", ".boo", ".sbx", ".zed", ".vem",
        ".vfs", ".sbx", ".sqz", ".xfp")


# checks if an extension is in one of the previous list and returns True, otherwise, returns False
def is_audio(file):
    return os.path.splitext(file)[1].lower() in audio


def is_video(file):
    return os.path.splitext(file)[1].lower() in video


def is_image(file):
    return os.path.splitext(file)[1].lower() in img


def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()


def is_ebook(file):
    return os.path.splitext(file)[1].lower() in ebook


def is_exe(file):
    return os.path.splitext(file)[1].lower() in exe


def is_zipped(file):
    return os.path.splitext(file)[1].lower() in zipped

def is_office(file):
    return os.path.splitext(file)[1].lower() in office

# creates directories if they don't exist
Path("audio").mkdir(exist_ok=True)
Path("video").mkdir(exist_ok=True)
Path("image").mkdir(exist_ok=True)
Path("screenshot").mkdir(exist_ok=True)
Path("ebook").mkdir(exist_ok=True)
Path("misc").mkdir(exist_ok=True)
Path("exe").mkdir(exist_ok=True)
Path("office").mkdir(exist_ok=True)
Path("compressed").mkdir(exist_ok=True)

# iterates on each file in the directory and if the extension is in one of the lists, move the file to the correct directory
for file in os.listdir():
    if is_audio(file):
        shutil.move(file, f"/Users/{username}/Downloads/audio")
    elif is_video(file):
        shutil.move(file, f"/Users/{username}/Downloads/video")
    elif is_ebook(file):
        shutil.move(file, f"/Users/{username}/Downloads/ebook")
    elif is_exe(file):
        shutil.move(file, f"/Users/{username}/Downloads/exe")
    elif is_zipped(file):
        shutil.move(file, f"/Users/{username}/Downloads/compressed")
    elif is_office(file):
        shutil.move(file, f"/Users/{username}/Downloads/office")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, f"/Users/{username}/Downloads/screenshot")
        else:
            shutil.move(file, f"/Users/{username}/Downloads/image")
    # else:
        # shutil.move(file, f"/Users/{username}/Downloads/misc")

# an output message
print(f"Files have been organized!")
