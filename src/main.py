
from domain.assistant import Assistant


while True:
    try:
        assistant = Assistant()
        assistant.listen()
        command = assistant.text
        if 'tell a joke' in command:
            assistant.tell_a_joke()
    except:
        pass