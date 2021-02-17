import spotipy
from exceptions.spotify import InvalidDeviceNameException
from exceptions.spotify.invalid_search_exception import InvalidSearchException
from settings.settings import Settings
from spotipy.oauth2 import SpotifyOAuth


class Spotify:
    """Spotify integration"""

    def __init__(self) -> None:
        self._authenticate()
        self.set_device(Settings.spotify.device_name)
        ## implementar historico
        self.history = []

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

    def _search_type(self, name: str, type: str):
        """Search in spotify.

        Args:
            name (str): Name to search.
            type (str): Type to search. One of 'artist', 'album', 'track', 'playlist'.

        Raises:
            InvalidSearchException: When not found any item of the search.

        Returns:
            tuple: First item is NAME found and second is URI.
        """
        name_to_search = name.replace(' ', '+')
        results = self._spotify.search(q=name_to_search, limit=1, type=type)
        items = results[f'{type}s']['items']
        if not items:
            raise InvalidSearchException(f'No {type} found {name}')
        uri = items[0]['uri']
        name = items[0]['name']
        return name, uri