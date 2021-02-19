from domain.assistant import Assistant
from helpers.check_is_in_command_helper import check_is_in_command_helper


def joke_command(func):
    def wrapper(command: str, assistant: Assistant):
        joke_commands = ['tell a joke', 'tell me a joke']
        is_in_command = check_is_in_command_helper(joke_commands, command)
        if is_in_command:
            assistant.tell_a_random_joke()
            return
        func(command, assistant)

    return wrapper
