import os

class Producto:
    def __init__(self,tipo,contenido,precio):
        self.tipo=tipo
        self.contenido=contenido
        self.precio=precio
        
    def datos(self):
        dato=[self.tipo,self.contenido,self.precio]
        return dato
    
    def product(self):
        print('Tipo: ',(self.tipo))
        print('Descripción: ',(self.contenido))
        print('Precio: ',(self.precio))
        
    def registro(self):
        t=input('Tipo: ')
        self.tipo=y
        c=input('Descripción: ')
        self.contenido=c
        p=input('Precio: ')
        self.precio=p
       
    def Crear_archivo(self):
        import pickle
        archivo=open('Productos','ab')
        d=self.datos()
        pickle.dump(d,archivo)
        archivo.close()
        
    def get_tipo(self):
        return self.tipo
    
    def get_contenido(self):
        return self.contenido

    def get_nombre(self):
        return self.precio
