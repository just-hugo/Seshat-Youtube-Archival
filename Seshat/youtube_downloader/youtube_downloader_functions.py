from pytube import YouTube


class YouTubeDownloader():

    def get_video_URLs(self):
        video_url = input("Please enter the URL of each YouTube video you want to download. Separate each URL by a comma: ")

        return video_url

    def download_video_from_url(self, urls_list, download_directory):
        for each_video_url in urls_list:
            # create YouTube object of the video at the URL provided
            video = YouTube(str(each_video_url))

            # download the video at the highest available resolution at the target directory
            video.streams.get_highest_resolution().download(download_directory)

            # get video title
            title = video.title

            print(f"{title} has been successfully downloaded to {download_directory}")
