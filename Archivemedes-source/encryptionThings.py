from cryptography.fernet import Fernet

def genKey():
    try:
        return Fernet.generate_key()
    except:
        return None

def encrypt(txt,key):
    try:
        return Fernet(key).encrypt(txt)
    except:
        return None