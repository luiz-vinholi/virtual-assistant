from domain.assistant import Assistant
from helpers.check_is_in_command_helper import check_is_in_command_helper


def spotify_command(func):
    def wrapper(command: str, assistant: Assistant):
        command_words = command.split(' ')
        first_command_word = command_words[0]
        stop_commands = ['stop', 'pause']
        resume_commands = ['resume', 'continue']
        is_stop_in_command = check_is_in_command_helper(
            stop_commands,
            first_command_word,
        )
        is_resume_in_command = check_is_in_command_helper(
            resume_commands,
            first_command_word,
        )
        if 'play' in first_command_word:
            name = command.replace('play', '')
            types = ['album', 'artist', 'track']
            for type in types:
                if type in name:
                    name = name.replace(type, '')
                    assistant.spotify.play(name, type)
                    return
            assistant.spotify.play(name, 'track')
            return
        elif is_stop_in_command:
            assistant.spotify.pause()
            return
        elif is_resume_in_command:
            assistant.spotify.resume()
            return
        func(command, assistant)
    return wrapper
