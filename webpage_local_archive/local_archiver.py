import requests
from functions.general_functions import Seshat
from local_archiver_functions import LocalArchiver

Seshat = Seshat()
archive = LocalArchiver()

# collect URL(s) from user and format them
user_webpage_urls = Seshat.get_URLs()
webpage_list = Seshat.format_user_URLs_as_list(user_webpage_urls)
formatted_webpage_urls = Seshat.add_url_prefix(webpage_list)

# TODO: make this capable of taking more than
# collect download directory and file name from user
download_directory = Seshat.get_download_directory()
webpage_name = archive.get_webpage_name()

# create the path of the download file
file_path = download_directory + "/" + webpage_name

for each_webpage in
webpage_html = requests.get(webpage).text

with open(rf"{file_path}", "w") as file:
    file.write(webpage_html)
