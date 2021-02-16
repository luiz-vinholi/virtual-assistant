import spotipy
from exceptions.spotify.invalid_device_name_exception import InvalidDeviceNameException
from settings.settings import Settings
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    """Spotify integration"""

    def __init__(self) -> None:
        self._authenticate()
        self.set_device(Settings.spotify.device_name)

    def set_device(self, device_name: str) -> None:
        """Set device to play musics Spotify.

        Args:
            device_name (str): Identifier of the connected device on Spotify.

        Raises:
            InvalidDeviceNameException: If device with device_name param not found or invalid.
        """
        device_id = None
        devices = self._spotify.devices()['devices']
        for device in devices:
            device['name'] = device['name'].replace('´', '\'')
            if device['name'] == device_name:
                device_id = device['id']

        if not device_id:
            raise InvalidDeviceNameException()
        self._device_id = device_id

    def _authenticate(self) -> None:
        """Authenticate on Spotify"""
        oauth_manager = SpotifyOAuth(
            client_id=Settings.spotify.client_id,
            client_secret=Settings.spotify.secret_key,
            redirect_uri=Settings.spotify.redirect_uri,
            username=Settings.spotify.username,
            scope=Settings.spotify.scope,
        )
        self._spotify = spotipy.Spotify(auth_manager=oauth_manager)
