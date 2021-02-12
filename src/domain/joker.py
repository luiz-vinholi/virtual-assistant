import pyjokes

from .talker import Talker


class Joker(Talker):
    def __init__(self) -> None:
        super(Joker, self).__init__()

    def tell_a_joke(self):
        joke = pyjokes.get_joke()
        self.talk(joke)
