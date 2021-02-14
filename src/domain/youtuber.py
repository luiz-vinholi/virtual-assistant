from pywhatkit import playonyt


class Youtuber:
    def play_video(self, title: str) -> None:
        """Open video on yotube from browser.

        Args:
            title (str): Video title.
        """
        playonyt(title)
