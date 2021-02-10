from domain.talker import Talker
from domain.listener import Listener


class Assistant(Talker, Listener):
    def __init__(self) -> None:
        super().__init__()

    
    