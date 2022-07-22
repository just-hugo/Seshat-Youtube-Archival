import unittest
from youtube_downloader import youtube_downloader_functions as func
from unittest.mock import patch
from functions.general_functions import Seshat

Seshat = Seshat()


class YouTubeDownloader(unittest.TestCase):

    def test_get_URLs_works(self):
        url = Seshat.get_URLs()
        print(url)


    def test_get_video_URLs_returns_string(self):
        user_input = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

        with patch('builtins.input', side_effect=user_input):

            returned_object = func.get_video_URLs()

            self.assertEqual(type(returned_object), str)

    def test_get_download_directory_returns_string(self):
        return


if __name__ == '__main__':
    unittest.main()
