import os
from pytube import Playlist, YouTube
from datetime import datetime


class Logger:
    RED = 91
    GREEN = 92
    WHITE = 00

    @staticmethod
    def print_colored(message, color):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\033[{}m{}\033[{}m" .format(
            color, f"{timestamp} \t {message}", Logger.WHITE))

    @staticmethod
    def info(message, color=WHITE):
        Logger.print_colored(message, color)

    @staticmethod
    def error(message, color=RED):
        Logger.print_colored(message, color)


class Utils:
    OUTPUT_FOLDER = './DOWNLOADED'

    @staticmethod
    def make_dir(name=None):
        if name is None:
            name = Utils.OUTPUT_FOLDER
        else:
            name = Utils.OUTPUT_FOLDER + "/" + name.split()[0]
        if not os.path.exists(name):
            os.makedirs(name)
        return name

    @staticmethod
    def get_playlist(url):
        try:
            playlist = Playlist(url)
            return playlist.title, playlist.video_urls
        except:
            Logger.error("Error getting playlist")

    @staticmethod
    def download_video(path, url, verbose=True):
        try:
            video = YouTube(url)
            stream = video.streams.get_highest_resolution()
            if verbose:
                Logger.info("Downloading " + stream.title)
            stream.download(output_path=path)
        except:
            Logger.error("Error downloading video")
