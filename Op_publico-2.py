import os
class publicacion:
    def __init__(self):
        self.lis=[]
    def leer(self):
        pub= "publicaciones.txt"
        if pub in os.listdir("."):
            print("\nArchivo creado en la ruta: \n\n\t{0}/{1}".format(os.getcwd(),pub))
        else:
            archivo = open(pub, "x")
            archivo.close()
        archivo = open(pub, "r")
        for linea in archivo:
            self.lis.append(linea)
        archivo.close()
    def mostrar(self):
        print(self.lis)
    def añadir(self):
        print("Ingresa los datos de la publicación: ")
        usuario=str(input("Tu nombre: "))
        lugar=str(input("Lugar de la reunión: "))
        fecha=str(input("Fecha de la reunion: "))
        publi=usuario+"\r"+lugar+"\r"+fecha+"\n"
        self.lis.append(publi)
    def modificarañadir(self):
        ar = "publicaciones.txt"
        archivo=open(ar,"w")
        for i in self.lis:
            archivo.write(i)
        archivo.close()
    def reiniciar(self):
        self.lis=[]
pub=publicacion()
opcion=-1
while opcion!="0":
    print("Qué quieres hacer?\n\t1-Crear una publicacion\n\t0-Cerrar")
    opcion=input("")
    if opcion=="1":
        pub.leer()
        pub.mostrar()
        pub.añadir()
        pub.modificarañadir()
        pub.reiniciar()
