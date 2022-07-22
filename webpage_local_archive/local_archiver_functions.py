class LocalArchiver():

    def get_webpage_name(self):
        webpage_name = input(
            "Please enter what you would like to name your download, including the extension \".html\": ")

        # find name of webpage from title tag of url
        #

        return webpage_name

    def make_file_path(self, download_directory, webpage_name):
        file_path = download_directory + "/" + webpage_name

        return file_path

    def write_webpage_to_file(self, file_path, webpage_html):
        with open(rf"{file_path}", "w") as file:
            file.write(webpage_html)
