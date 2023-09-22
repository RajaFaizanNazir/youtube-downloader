from utils import Utils, Logger

Utils.make_dir()

playlist = "https://www.youtube.com/playlist?list=PLF9mJC4RrjIhS4MMm0x72-qWEn1LRvPuW"

title, videos = Utils.get_playlist(playlist)
path = Utils.make_dir(title)
for video in videos:
    Utils.download_video(path, video)

Logger.info("Download Completed", Logger.GREEN)
