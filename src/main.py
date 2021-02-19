
from domain.assistant import Assistant
from helpers.command_orchestrator_helper import command_orchestrator_helper


assistant = Assistant()
while True:
    assistant.listen()
    command = assistant.command
    if command:
        command_orchestrator_helper(command, assistant)
