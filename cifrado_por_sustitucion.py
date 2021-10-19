#Elaboró Jose Antonio Rivera Torres 
#Carrera en Ingneria en sistemas computacionales
import random
# recibe el mensaje del usuario
mensaje_1 = ""
# valores aleatorios para la clave


# encriptar el mensaje
def encriptar(msg, clave):
    # mensaje encriptado
    encriptado = ""
    for i in msg:
        encriptado += chr(ord(i)+clave)
    # generamos clave
    clave+= len(encriptado)
    clave = chr(clave)
    # cocateno la clave con el mensaje
    encriptado += clave
    return encriptado

# decodifica el mensaje
def decodificar(msg):
    # obtener clave de la cadena
    clave = ord(msg[-1]) + 1 
    clave -= len(msg)
    # eliminamos la clave
    msg = msg[:-1]
    mensaje_2 = ""
    for j in msg:
        # guardamos el mensaje desencriptado
        mensaje_2 += chr(ord(j)-clave)
    # retornamos el mensaje desencriptado
    return mensaje_2
    
#contador
n = 1
print(f"************************* CHAT WHOAMI {n} *********************** ")
while(True):
    #generamos clave
    clave = random.randint(1,30)
    # mensaje
    mensaje_1 = input("Ingrese el mensaje >_ ")
    msg_encriptado = encriptar(mensaje_1, clave)
    msg_decodificado = decodificar(msg_encriptado)
    n+=1
    print("\n"*3)
    print(f"************************* CHAT WHOAMI {n} *********************** ")
    print("--------------------------------------------------------------- ")
    print(f"Mensaje encriptado --> {msg_encriptado}")
    print("--------------------------------------------------------------- ")
    print(f"Mensaje recibido --> {msg_decodificado}")
