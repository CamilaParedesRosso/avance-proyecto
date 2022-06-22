import os

class Promocion:
    def __init__(self,empresa,tipo,promo,precio,tiempo):
        self.empresa=empresa 
        self.tipo=tipo
        self.promo=promo
        self.precio=precio
        self.tiempo=tiempo
        
    def lista(self):
        l=[self.empresa,self.tipo,self.promo,self.precio,self.tiempo]
        return l
    
    def mostrarpromo(self):
        print(self.empresa)
        print('Tipo: ',(self.tipo))
        print('Promo: ',(self.promo))
        print('Precio: ',(self.precio))
        print('Duración: ',(self.tiempo))
        
    def registro(self):
        e=input('Empresa: ')
        self.empresa=e
        t=input('Tipo: ')
        self.tipo=t
        p=input('Promo: ')
        self.promo=p
        pr=input('Precio: ')
        self.edad=pr 
        d=input('Duración: ')
        self.tiempo=d
        
    def Crear_archivo(self):
        import pickle
        archivo=open('Promociones','ab')
        s=self.l()
        pickle.dump(s,archivo)
        archivo.close()
        
    def get_empresa(self):
        return self.empresa
    
    def get_tipo(self):
        return self.tipo

    def get_promo(self):
        return self.promo
    
    def get_precio(self):
        return self.precio
    
    def get_tiempo(self):
        return self.tiempo
