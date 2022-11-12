from cryptography.fernet import Fernet

# Generate Fernet key
def genKey():
    try:
        return Fernet.generate_key()
    except:
        return None

def encrypt(content,key):
    try:
        return Fernet(key).encrypt(content)
    except:
        return None