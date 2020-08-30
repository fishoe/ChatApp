import os

from asgiref.sync import sync_to_async
from tensorflow.keras.preprocessing.sequence import pad_sequences

from .models import User

@sync_to_async
def checkHateWord(name, model, tokenizer, text):
    user = User.objects.get(name = name)
    model = model if model else None

    token_stc = text.split()
    encode_stc = tokenizer.texts_to_sequences([token_stc])
    pad_stc = pad_sequences(encode_stc, maxlen = 50)

    scorelist = []
    for m in model :
        s = m.predict(pad_stc)[0][0]
        scorelist.append(s)
    print(pad_stc, scorelist)
    if max(scorelist) > 0.50:
        user.count += 1
        user.save()
    return str(user.count), max(scorelist)


def checkBlockUser(name):
    user = User.objects.get(name = name)
    if user.count > 4:
        user.blocked = True
    return user.blocked