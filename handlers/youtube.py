from pytube import Playlist, YouTube
from .logger import Logger


class YouTubeHandler:
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
            return stream.title
        except:
            Logger.error("Error downloading video")
