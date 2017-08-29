import pyrebase
import os


def getIdols():
    config = {
        "apiKey": os.environ['apiKey'],
        "authDomain": os.environ['authDomain'],
        "databaseURL": os.environ['databaseURL'],
        "storageBucket": os.environ['storageBucket'],
        "serviceAccount": os.environ['serviceAccount']
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    idols = db.child("idols").get()
    for idol in idols.each():
        yield idol.key()

