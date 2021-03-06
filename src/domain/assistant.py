from typing import Optional
from domain.integrations.spotify import Spotify

from domain.joker import Joker
from domain.listener import Listener
from domain.talker import Talker
from domain.integrations.youtube import Youtube
from exceptions import spotify


class Assistant(Listener, Joker, Talker):
    def __init__(self, name: str = 'alexa', activate_me_with: Optional[str] = 'hey') -> None:
        super(Assistant, self).__init__()
        self.name: str = name
        self.activate_me_with: Optional[str] = activate_me_with
        self.is_talking_to_me: bool = False
        self.command: Optional[str] = None
        self._activation_command: str = f'{self.activate_me_with} {self.name}' \
            .strip()
        self._init_integrations()

    def listen(self) -> None:
        super().listen()
        self.is_talking_to_me = self._activation_command in self.text
        if self.is_talking_to_me:
            self.command = self.text.replace(self._activation_command, '') \
                .strip()

    def _init_integrations(self):
        try:
            self.youtube = Youtube()
            self.spotify = Spotify()
        except spotify.InvalidDeviceNameException:
            self.talk('Verify Spotify device name in dot env file')
