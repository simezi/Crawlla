import pyrebase
import os

from collections import defaultdict

config = {
    "apiKey": os.environ['apiKey'],
    "authDomain": os.environ['authDomain'],
    "databaseURL": os.environ['databaseURL'],
    "storageBucket": os.environ['storageBucket'],
    "serviceAccount": os.environ['serviceAccount']
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()

songIdols = db.child("songIdols").get()

idolSongs = defaultdict(dict)

for songIdol in songIdols.each():
    if not 'idols' in songIdol.val():
        continue
    idols = songIdol.val()['idols']
    for idol in idols:
        idolSongs[idol].update({songIdol.key():True})


# [print(idolSong) for idolSong in idolSongs]
print(idolSongs)
db.child("idolSongs").set(idolSongs)
