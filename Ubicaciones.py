import os

class Direccion:
    def __init__(self,zona,avenida,calle,numero,referencia):
        self.zona=zona
        self.avenida=avenida 
        self.calle=calle
        self.numero=numero
        self.referencia=referencia 
        
    def datos(self):
        dato=[self.zona,self.avenida,self.calle,self.numero,self.referencia]
        return dato
    
    def mostrardireccion(self):
        print('Dirección: ',(self.zona),(self.avenida),(self.calle),(self.numero),(self.referencia)
        
    def registro(self):
        z=input('Zona: ')
        self.zona=z
        a=input('Avenida: ')
        self.avenida=a
        c=input('Calle: ')
        self.calle=c
        n=input('N: ')
        self.numero=n
        r=input('Referencia: ')
        self.referencia=r
        
    def Crear_archivo(self):
        import pickle
        archivo=open('Direccion','ab')
        d=self.datos()
        pickle.dump(d,archivo)
        archivo.close()
        
    def get_zona(self):
        return self.zona
    
    def get_avenida(self):
        return self.avenida

    def get_calle(self):
        return self.calle
    
    def get_numero(self):
        return self.numero
    
    def get_referencia(self):
        return self.referencia
