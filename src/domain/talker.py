import pyttsx3


class Talker:
    def __init__(self) -> None:
        self._engine = pyttsx3.init()
        voices = self._engine.getProperty('voices')
        for voice in voices:
            if voice.languages[0] == u'en-us':
                self._engine.setProperty('voice', voice.id)
                break

    def talk(self, text: str) -> None:
        self._engine.say(text)
        self._engine.runAndWait()
    
