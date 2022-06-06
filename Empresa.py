import os

class Empresa:
    def __init__(self,usuario,contrasena,nombre,correo,telefono,direccion):
        self.usuario=usuario
        self.contrasena=contrasena
        self.nombre=nombre
        self.correo=correo
        self.telefono=telefono
        self.direccion=direccion
                
    def datos(self):
        dato=[self.usuario,self.contrasena,self.nombre,self.correo,self.telefono,self.direccion]
        return dato
    
    def mostrar_datos(self):
        print('Usuario: ',(self.correo))
        print('Nombre de la Empresa: ',(self.telefono))
        print('Correo: ',(self.correo))
        print('Telefono: ',(self.telefono))
        print('Direccion: ',(self.direccion))
    
    def registro_usuario(self):
        u=input('Usuario: ')
        self.usuario=u
        co=input('Contraseña: ')
        self.contrasena=co
        
    def registro(self):
        n=input('Nombre de la empresa: ')
        self.nombre=n
        c=input('Correo: ')
        self.correo=c
        t=input('Teléfono: ')
        self.telefono=t
        e=input('Direccion: ')
        self.edad=e

    def Crear_archivo(self):
        import pickle
        archivo=open('Empresa','ab')
        d=self.datos()
        pickle.dump(d,archivo)
        archivo.close()
        
    def get_usuario(self):
        return self.usuario
    
    def get_contrasena(self):
        return self.contrasena

    def get_nombre(self):
        return self.nombre
    
    def get_correo(self):
        return self.correo
    
    def get_telefono(self):
        return self.telefono
    
    def get_direccion(self):
        return self.direccion
