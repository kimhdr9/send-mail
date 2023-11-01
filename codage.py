from cryptography.fernet import Fernet
import os

def chaine(binaire):
    """
    transforme un binaire en chaine de caractère utf8
    """
    return str(binaire,'utf8')

def info(message,variable):
    """
    affiche un message avec la variable associée
    """
    print(f'{message} {variable}')

"""
crée une clé pour initier le cryptage
"""
if not os.getenv('KEY') :
    key = Fernet.generate_key()
else :
    key= os.getenv('KEY')
    key=b'{key}'

info('clé',chaine(key))
"""
cryptage d'un mot de passe
"""
crypter = Fernet(key)

pw=crypter.encrypt(b'MotDePasse')

info('mot de passe crypté',chaine(pw))

decrypte=crypter.decrypt(pw)

info('mot de passe décrypté',chaine(decrypte))