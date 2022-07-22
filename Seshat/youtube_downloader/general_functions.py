class Seshat():

    def get_URLs(self):
        user_url = input(
            "Please enter the URL. Separate each URL by a comma: ")

        webpage_prefix = user_url[0] + user_url[1] + user_url[2]

        if webpage_prefix != "htt":

            if webpage_prefix == "www":
                new_url = "http://" + user_url
                return new_url

            if webpage_prefix != "www":
                new_url = "http://www." + user_url
                return new_url
        else:
            return user_url

    def format_user_URLs_as_list(self, user_urls):
        urls_list = user_urls.split(",")

        return urls_list

    def add_url_prefix(self, urls_list):
        """requests library will not make a request with partial urls, so it is necessary to check whether user-inputted urls contain the full set of prefixes and add them if not
        """

        # a place to store each url once it has been checked and formatted
        formatted_urls = []

        for each_url in urls_list:

            # identify the first three characters of the url
            webpage_prefix = each_url[0] + each_url[1] + each_url[2]

            # adds a hyperlink prefix to any urls without one
            if webpage_prefix != "htt":

                new_url = "http://" + each_url
                formatted_urls.append(new_url)

            # adds urls that do not need formatting to the list
            else:
                formatted_urls.append(each_url)

        return formatted_urls

    def get_download_directory(self):
        download_directory = input("Please enter the absolute path of the directory you would like to download to: ")

        return download_directory