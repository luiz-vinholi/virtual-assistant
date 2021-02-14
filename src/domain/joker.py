import pyjokes

from .talker import Talker


class Joker(Talker):
    """Jokes teller."""

    def __init__(self) -> None:
        super(Joker, self).__init__()

    def tell_a_random_joke(self) -> None:
        """Make a sound telling a random joke."""
        joke = pyjokes.get_joke()
        self.talk(joke)
