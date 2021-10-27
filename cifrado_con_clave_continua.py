#Elaboró Jose Antonio Rivera Torres
#Carrera Ing. en Sitemas Computacionales

import random
from operator import xor

#lista = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

# generar clave
def generateKey(len_msg):
    key = ""
    for i in range(len(len_msg)):
        key += chr(random.randint(97, 130))
    return key


# operacion XOR
def operationXOR(letter_a, lleter_b):
    return chr(xor(ord(letter_a), ord(lleter_b)))

# encriptar el mensjae
def encrypt(msg,key):
    msg_encrypted = ""
    for i in range(len(msg)):
        msg_encrypted += operationXOR(msg[i], key[i])
    return msg_encrypted


# desencriptar mensaje
def decrypt(msg, key):
    msg_decrypted = ""
    for i in range(len(msg)):
        msg_decrypted += operationXOR(msg[i], key[i])
    return msg_decrypted


msg_usr = input("Ingresa el mensaje: ")
key = generateKey(msg_usr)
msg_encrypted_generte = encrypt(msg_usr,key)
msg = decrypt(msg_encrypted_generte,key)
print(f"Clave: {key}")
print(f"Mensaje encriptado {msg_encrypted_generte}")
print(f"Mensja decodificado {msg}")
