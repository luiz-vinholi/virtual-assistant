from domain.joker import Joker
from domain.talker import Talker
from domain.listener import Listener


class Assistant(Listener, Joker, Talker):
    def __init__(self) -> None:
        super(Assistant, self).__init__()
