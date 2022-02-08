import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

class DataBase:

    @staticmethod
    def checkCD(cooldown):
        dif = cooldown - DataBase.getTimestamp()
        difSec = dif.total_seconds()
        m, s = divmod(difSec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        if difSec < 0:
            cdStatus = 'Disponível'
        else:
            cdStatus = f'{int(d) if d > 0 else 0}d {int(h)}:{int(m)}h'
        return cdStatus

    @staticmethod
    def getTimestamp():
        time = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
        return time

    @staticmethod
    def createUser(id):
        userData = db.collection('users').document(id).get()
        if userData.exists:
            return 0
        else:
            db.collection('users').document(id).set({
                'id': id,
                'entrada': DataBase.getTimestamp(),
                'dailyCD': DataBase.getTimestamp(),
                'weeklyCD': DataBase.getTimestamp(),
                'xp': 0,
                'coin': 1000
                })

    @staticmethod
    def getData(id: str, *args, **kwargs):
        userData = db.collection('users').document(id).get()
        if userData.exists:
            return userData.to_dict()
        else:
            return 0

    @staticmethod
    def saveData(id: str, *args, **kwargs):
        db.collection('users').document(id).update(kwargs)