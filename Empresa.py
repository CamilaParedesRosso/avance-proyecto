import os

class Empresa:
    def __init__(self,nombre,correo,telefono,direccion):
        self.nombre=nombre
        self.correo=correo
        self.telefono=telefono
        self.direccion=direccion
                
    def lista(self):
        l=[self.nombre,self.correo,self.telefono,self.direccion]
        return l
    
    def perfil(self):
        print(self.nombre)
        print(f'Correo: {self.correo}')
        print(f'Telefono: {self.telefono}')
        print(f'Direccion: {self.direccion}')
        
    def registro(self):
        n=input('Nombre de la empresa: ')
        self.nombre=n
        c=input('Correo: ')
        self.correo=c
        t=input('Teléfono: ')
        self.telefono=t
        e=input('Direccion: ')
        self.edad=e
        

    def get_nombre(self):
        return self.nombre
    
    def get_correo(self):
        return self.correo
    
    def get_telefono(self):
        return self.telefono
    
    def get_direccion(self):
        return self.direccion
