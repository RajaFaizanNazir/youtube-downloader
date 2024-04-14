from handlers import Logger
from handlers import Utils
from handlers import YouTubeHandler

Utils.make_dir()


def download_playlist(playlist, verbose=True):
    title, videos = YouTubeHandler.get_playlist(playlist)
    path = Utils.make_dir(title)
    for video in videos:
        YouTubeHandler.download_video(path, video, verbose=verbose)
    Logger.info("Download Completed", Logger.Color.GREEN)


playlist_url = "https://www.youtube.com/playlist?list=PLF9mJC4RrjIhS4MMm0x72-qWEn1LRvPuW"
download_playlist(playlist_url)
