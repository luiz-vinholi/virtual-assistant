import pyttsx3


class Talker:
    def __init__(self) -> None:
        super(Talker, self).__init__()
        self._engine = pyttsx3.init()
        voices = self._engine.getProperty('voices')
        self._engine.setProperty('rate', 100) 
        for voice in voices:
            if voice.languages[0] == u'en-us':
                self._engine.setProperty('voice', voice.id)
                break

    def talk(self, text: str) -> None:
        self._engine.say(text)
        self._engine.runAndWait()
    
