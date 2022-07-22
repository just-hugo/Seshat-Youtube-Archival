from pytube import YouTube

# collect URL(s) from user
video_url = input("Please enter the URL of each YouTube video you want to download. Separate each URL by a comma: ")

# collect download directory from user
download_directory = input("Please enter the directory where you want the video(s) to be downloaded: ")

# format csv list of URLs into a Python list
urls_list = video_url.split(",")

for each_video_url in urls_list:
    # create YouTube object of the video at the URL provided
    video = YouTube(str(each_video_url))

    # download the video at the highest available resolution at the target directory
    video.streams.get_highest_resolution().download(download_directory)

    # get video title
    title = video.title

    print(f"{title} has been successfully downloaded to {download_directory}")

print("Ending program.")