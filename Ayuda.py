import os
from datetime import datetime
fecha=str(datetime.today())
def chat():
    chat = "chat.txt"
    if chat in os.listdir("."):
        print("\nArchivo creado en la ruta: \n\n\t{0}/{1}".format(os.getcwd(),chat))
    else:
        archivo = open(chat, "x")
        archivo.close()
    archivo = open(chat, "w")
    texto="\n"+fecha+"\t Daniela: buenos dias, yo quiero ir."
    archivo.write(texto)
    archivo.close()
    archivo = open(chat, "r")
    for linea in archivo:
        print(linea , "\n")
    archivo = open(chat, "w")
    texto="\n"+fecha+"\t Daniela: buenos dias, yo quiero ir."
    archivo.write(texto)
    texto="\n"+fecha+"\t Mario: Bien!"
    archivo.write(texto)
    archivo.close()
    return