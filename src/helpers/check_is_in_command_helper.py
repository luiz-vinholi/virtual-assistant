from typing import List


def check_is_in_command_helper(texts: List[str], command: str) -> bool:
    is_in_command: bool = False
    for text in texts:
        if text in command:
            is_in_command = True
            break
    return is_in_command