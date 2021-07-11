from cryptography.fernet import Fernet


def decryption(unque_id,password):   
    unque_id=unque_id.encode()
    password=password.encode()
    f=Fernet(unque_id)
    decrypted=f.decrypt(password).decode()
    return decrypted