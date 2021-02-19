from domain.assistant import Assistant
from helpers.check_is_in_command_helper import check_is_in_command_helper


def youtube_command(func):
    def wrapper(command: str, assistant: Assistant):
        youtube_commands = ['play on youtube', 'open on youtube']
        is_in_command = check_is_in_command_helper(youtube_commands, command)
        if is_in_command:
            title = command.replace('play on youtube', '')
            assistant.play_video(title)
            return
        func(command, assistant)
    return wrapper
