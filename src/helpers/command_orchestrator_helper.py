from decorators.commands import joke_command, spotify_command, youtube_command
from domain.assistant import Assistant


@joke_command
@youtube_command
@spotify_command
def command_orchestrator_helper(command: str, assistant: Assistant):
    pass
