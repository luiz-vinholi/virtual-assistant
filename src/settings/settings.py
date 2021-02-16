from dotenv import load_dotenv

from .spotify_settings import SpotifySettings

load_dotenv()


class Settings:
    spotify: SpotifySettings = SpotifySettings()
