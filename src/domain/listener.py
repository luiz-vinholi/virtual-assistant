from typing import Any
from speech_recognition import Microphone, Recognizer


class Listener:
    def __init__(self) -> None:
        self._recognizer = Recognizer()
        self._recognizer.energy_threshold = 4000

    def listen(self):
        with Microphone() as source:
            print('listening...')
            self._recognizer.adjust_for_ambient_noise(source)
            audio_listened = self._recognizer.listen(source)
            text_listened: Any = self._recognizer.recognize_google(audio_listened)
            self.text: str = text_listened.lower()
            print(self.text)
