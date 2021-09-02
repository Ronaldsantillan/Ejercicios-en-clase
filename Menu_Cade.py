
from Ope_Cadena import Cadena
import os
class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print (opcion)
        opc=input("Elija una opcion[1...{}]: ".format(len(self.opciones)))
        return opc
opc = ""
while opc !="7":
        os.system("clear")
        men = Menu("Menu Operaciónes de Cadenas",["1)Recorrer Cadena", "2)Buscar Caracter", "3)Lista Posiciones","4)Lista Palabras", "5)cadena Lista", "6)Concatenar cadena", "7)Salir"])
        opc = men.menu()

        if opc=="1":
                os.system("clear")      
                cond=Cadena()
                print(cond.recorrerCadena())
                input("presiona una tecla pa continuar...")

        elif opc=="2":
                os.system("clear")
                cond=Cadena()
                print(cond.buscarCaracter())
                input("presiona una tecla pa continuar...")

        elif opc=="3":
                os.system("clear")
                cond=Cadena()
                print(cond.listaPosiciones())
                input("presiona una tecla pa continuar...")

        elif opc=="4": 
                os.system("clear")
                cond=Cadena()
                print(cond.listaPalabras())
                input("presiona una tecla pa continuar...")

        elif opc=="5":
                os.system("clear")
                cond=Cadena()
                print(cond.cadenaLista())   
                input("presiona una tecla pa continuar...")

        elif opc=="6":
                os.system("clear")
                cond=Cadena()
                print(cond.concatenarCadena())   
                input("presiona una tecla pa continuar...")

        elif opc=="7":
                os.system("clear")
                print ("Gracias por la utilizacion")
                print ("Vuelva pronto")        
        else :
                os.system("clear")
                print("Opcion no valida") 