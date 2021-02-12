from typing import Optional

from domain.joker import Joker
from domain.listener import Listener
from domain.talker import Talker


class Assistant(Listener, Joker, Talker):
    def __init__(self, name: str = 'alexa', activate_me_with: Optional[str] = 'hey') -> None:
        super(Assistant, self).__init__()
        self.name = name
        self.activate_me_with = activate_me_with
        self.is_talking_to_me = False
        self.command = None
        self._activation_command = f'{self.activate_me_with} {self.name}'.strip(
        )

    def listen(self):
        super().listen()
        self.is_talking_to_me = self._activation_command in self.text
        if self.is_talking_to_me:
            self.command = self.text.replace(self._activation_command, '') \
                .strip()
