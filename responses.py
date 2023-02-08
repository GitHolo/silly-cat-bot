import random

def handle_response(message) -> str:
    pmessage = message.lower()

    if pmessage == 'elo':
        return 'elo'

    if pmessage == 'roluj':
        return str(random.randint(1,6))

    if pmessage == '!help':
        return "`elo/roluj`"

    return "ktco"