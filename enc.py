from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encryption(passw):
    password_provide = "password"
    password = password_provide.encode()
    salt= os.urandom(16)
    kdf= PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key=base64.urlsafe_b64encode(kdf.derive(password))

    data = passw
    data = data.encode()
    f = Fernet(key)
    encrypte = f.encrypt(data)
    
    return {"token":key,
    "password":encrypte}


