import general_functions
from youtube_downloader_functions import YouTubeDownloader

Seshat = general_functions.Seshat()
YouTube = YouTubeDownloader()

# collect URL(s) from user
video_urls = YouTube.get_video_URLs()

# collect download directory from user
download_directory = Seshat.get_download_directory()

# format csv list of URLs into a Python list
urls_list = Seshat.format_user_URLs_as_list(video_urls)

# download the videos to the target directory
YouTube.download_video_from_url(urls_list, download_directory)

print("Ending program.")