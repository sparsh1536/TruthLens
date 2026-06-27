from yt_dlp import YoutubeDL
import os

# Folder where downloaded audio will be stored
DOWNLOAD_FOLDER = "../data/audio"

# Create the folder if it doesn't exist
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def download_audio(url: str):
    """
    Downloads the best available audio from a YouTube video.
    Returns the exact path of the downloaded audio file.
    """

    options = {
        "format": "bestaudio/best",
        "outtmpl": f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
        "quiet": False,
    }

    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    print("✅ Audio downloaded successfully!")

    return filename