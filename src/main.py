
from domain.assistant import Assistant
from domain.integrations.spotify import Spotify

def command_orchestrator(command: str):
    command_words = command.split(' ')
    first_command_word = command_words[0]
    if 'tell a joke' in command:
        assistant.tell_a_random_joke()
    elif 'play on youtube' in command:
        title = command.replace('play on youtube', '')
        assistant.play_video(title)
    elif 'play' in first_command_word:
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

while True:
    assistant = Assistant()
    assistant.listen()
    command = assistant.command
    if command:
        command_orchestrator(command)
