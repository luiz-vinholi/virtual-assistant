import os


class SpotifySettings:
    def __init__(self) -> None:
        self.client_id: str = os.getenv('SPOTIFY_CLIENT_ID') or ''
        self.secret_key: str = os.getenv('SPOTIFY_SECRET_KEY') or ''
        self.username: str = os.getenv('SPOTIFY_USERNAME') or ''
        self.device_name: str = os.getenv('SPOTIFY_DEVICE_NAME') or ''
        self.redirect_uri: str = os.getenv('SPOTIFY_REDIRECT_URI') or ''
        self.scope: str = os.getenv('SPOTIFY_SCOPE') or ''
