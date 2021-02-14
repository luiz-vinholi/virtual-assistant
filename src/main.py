
from domain.assistant import Assistant
import pywhatkit


def command_orchestrator(command: str):
    if 'tell a joke' in command:
        assistant.tell_a_random_joke()
    elif 'play on youtube' in command:
        title = command.replace('play on youtube', '')
        assistant.play_video(title)

while True:
    assistant = Assistant()
    assistant.listen()
    command = assistant.command
    if command:
        command_orchestrator(command)
