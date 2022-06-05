import pickle
import os
import Archivo
import Publico
import Organizar
import Empresa
import AddDelete
import Ayuda

print('Bienvenid@ a MeetPle')
print('Organiza salidas con tus amigos o conociendo personas. Planea salidas.')
input('Enter')

#Menu Publico
#MenuEmpresa

op1=0
while op1!=5:
    print('Deseas iniciar como: ')
    print('1. Publico')
    print('2. Empresa')
    print('5. Salir')
    op1=int(input('Digita la opcion que deseas: '))
    if op1==1:
        p=Publico()
        
    elif op1==2:
        e=Empresa()
        
    else:
        input('Digite un opcion valida: ')
        