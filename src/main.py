
from domain.assistant import Assistant


def command_orchestrator(command):
    if 'tell a joke' in command:
        assistant.tell_a_joke()


while True:
    assistant = Assistant()
    assistant.listen()
    command = assistant.command
    if command:
        command_orchestrator(command)
