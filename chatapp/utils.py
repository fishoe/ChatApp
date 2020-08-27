from asgiref.sync import sync_to_async

from .models import User

@sync_to_async
def checkHateWord(name, text):
    user = User.objects.get(name = name)
    # add 1 in user.count when text is hate word
    if text:
        user.count += 1
        user.save()
    return str(user.count)


def checkBlockUser(name):
    user = User.objects.get(name = name)
    if user.count > 4:
        user.blocked = True
        user.save()
    return user.blocked