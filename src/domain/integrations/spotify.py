from typing import List, Tuple
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
        self._history: List[Tuple[str, str]] = []

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value: Tuple[str, str]) -> None:
        if len(self._history) > 10:
            del self._history[-1]
        self._history.insert(0, value)

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

    def play(self, name: str, type: str) -> None:
        """Play track, album, playlist or artist by name. 

        Args:
            name (str): Name to search music.
            type (str): Playback type. One of 'artist', 'album', 'track', 'playlist'.
        """
        name_and_uri = self._search(name, type)
        self.history = name_and_uri
        _, uri = name_and_uri
        if type == 'track':
            uri_param = {'uris': [uri]}
        else:
            uri_param = {'context_uri': uri}
        self._spotify.start_playback(
            device_id=self._device_id,
            **uri_param,
        )

    def resume(self):
        """Resume playback."""
        self._spotify.start_playback(self._device_id)

    def pause(self):
        """Pause playback."""
        self._spotify.pause_playback(self._device_id)

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

    def _search(self, name: str, type: str) -> Tuple[str, str]:
        """Search in spotify and set in history.

        Args:
            name (str): Name to search.
            type (str): Type to search. One of 'artist', 'album', 'track', 'playlist'.

        Raises:
            InvalidSearchException: When not found any item of the search.

        Returns:
            Tuple[str, str]: First item in tuple is NAME found and second is URI.
        """
        name_to_search = name.replace(' ', '+')
        results = self._spotify.search(q=name_to_search, limit=1, type=type)
        items = results[f'{type}s']['items']
        if not items:
            raise InvalidSearchException(f'No {type} found {name}')
        uri = items[0]['uri']
        name = items[0]['name']
        return name, uri
