from decorators.commands import joke_command, youtube_command
from domain.assistant import Assistant


@joke_command
@youtube_command
def command_orchestrator_helper(command: str, assistant: Assistant):
    command_words = command.split(' ')
    first_command_word = command_words[0]
    if 'play' in first_command_word:
        name = command.replace('play', '')
        types = ['album', 'artist', 'track']
        for t in types:
            if t in name:
                name = name.replace(t, '')
                assistant.spotify.play(name, type=t)
                return
            assistant.spotify.play(name, 'track')
    elif 'stop' in first_command_word or 'pause' in first_command_word:
        assistant.spotify.pause()
    elif 'continue' in first_command_word or 'resume' in first_command_word:
        assistant.spotify.resume()
