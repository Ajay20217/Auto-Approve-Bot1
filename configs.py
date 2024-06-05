from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "11893421"))
    API_HASH = getenv("API_HASH", "f571101b32748bc6f8e2178d03c12dd0")
    BOT_TOKEN = getenv("BOT_TOKEN", "7023173279:AAF8YCrCbZH6Z2hhwVZjIe945YuUpC-mzKA")
    FSUB = getenv("FSUB", "0")
    CHID = int(getenv("CHID", "-1001939184003"))
    SUDO = list(map(int, getenv("SUDO","6036497605").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://naibansari987:Yuuichi@cluster0.vbota1p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()
