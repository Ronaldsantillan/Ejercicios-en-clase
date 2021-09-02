BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import os
class Basico:
    def __init__(self):
       pass 
    def numerosN(self):
        n1=int(input(GREEN+"ingrese el primer numero:"))
        n2=int(input(GREEN+"ingrese el segundo numero:"))
        for x in range(n1,n2):
            print (x)

    def multiplo(numero):
        numero=int(input(GREEN+"ingrese el numero que desea saber el mutliplo:"))
        n1=int(input(GREEN+"ingrese el multiplo:"))
        if numero % n1 ==0:
            print (YELLOW+"el numero: {} si es multiplo de: {}".format(numero,n1))
        else:
            print(YELLOW+"el numero: {} si es multiplo de: {}".format(numero,n1))


    def Divisoresnumero(numero):
        numero=int(input(GREEN+"ingrese el numero:"))
        divisores=[]
        for i in range(1,numero+1):
            if numero % i==0:
                divisores.append(i)
        print(divisores)
        
    def Primo(numero):
        numero=int(input(GREEN+"ingrese el numero:"))
        if numero>1:
            cont=0
            for i in range(2,numero):
                residuo=numero%i 
                print("{} % {} = {}".format(numero,i,residuo)) 
                if residuo == 0:
                    cont+=1
            if cont==0:
                print("El {} es un número primo".format(numero))  
            else:
                print("el {} no es un número primo".format(numero))
        else:
            print("el {} no es un número primo".format(numero))

    def perfecto(numero):
        numero=int(input(GREEN+"Ingrese el numero que desee saber si es perfeto:"))
        j=0
        for i in range(1,numero):
            if numero%i==0:
                j = j+i
        if (j==numero):
            print(YELLOW+"el número {} es perfecto".format(numero))
        else:
            print(YELLOW+"el número {} no es perfecto".format(numero))

class Intermedio(Basico):
    def numerosN(self):
        suma=0
        n1=int(input(GREEN+"ingrese el primer numero:"))
        n2=int(input(GREEN+"ingrese el segundo numero:"))
        for i in range(n1,n2+1):
            suma += i
            print(YELLOW+"{}".format(suma))

    def factorial(numero):
        numero=int(input(GREEN+"ingrese un numero:"))
        factorial=1
        for n in range(1,(numero+1)):
            factorial=factorial*n
        print (YELLOW+"el factorial de {} es: {}".format(numero,factorial))

    def fibonacci(n):
        e=0
        d=1
        n=int(input(GREEN+"Ingrese los n terminos que desea imprimir:"))
        if n==0:
            print(YELLOW+e)
        elif n==1:
            print(e)
            print(d)
        else:
            print(e)
            print(d)

            for i in range(n-2):
                c=e+d
                if i == n-3:
                 print(c)
                else:
                    print(c)
                    e=d
                    d=c
# cond=Intermedio()
# cond.fibonacci()
GREEN = '\033[32m'
import os
from rango import Basico,Intermedio
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
while opc !="11":
        os.system("clear")
        menuC= Menu(GREEN+"Menu Principal",["1) Presentar los números de 1 a n","2) Sumar los números de 1 a n","3) Múltiplo de cualquier numero","4) Presentar los divisores de un numero","5) Numero Primo","6) Factorial de cualquier numero",
        "7) Fibonacci de una serie de n número","8) Perfecto","9) Primos gemelos","10) Números amigos","11)	Salir"])
        opc=menuC.menu()

        if opc=="1":
                os.system("clear")      
                cond=Basico()
                print(cond.numerosN())
                input("presiona una tecla pa continuar...")
                
                
        elif opc=="2":
                os.system("clear")
                cond=Intermedio()
                print(cond.numerosN())
                input("presiona una tecla pa continuar...")
                
        elif opc=="3":
                os.system("clear")
                cond=Basico()
                print(cond.multiplo())
                input("presiona una tecla pa continuar...")

        elif opc=="4": 
                os.system("clear")
                cond=Basico()
                print(cond.Divisoresnumero())
                input("presiona una tecla pa continuar...")
                        
        elif opc=="5":
                os.system("clear")
                cond=Basico()
                print(cond.Primo())   
                input("presiona una tecla pa continuar...")

        elif opc=="6":
                os.system("clear")
                cond=Intermedio()
                print(cond.factorial())   
                input("presiona una tecla pa continuar...")
                        
        elif opc=="7":
                os.system("clear")
                cond=Intermedio()
                print(cond.fibonacci())   
                input("presiona una tecla pa continuar...")
                        
        elif opc=="8":
                os.system("clear")
                cond=Basico()
                print(cond.perfecto())   
                input("presiona una tecla pa continuar...")
                        
        elif opc=="9":
                os.system("clear")
                print ("Primos gemelos")
                        
        elif opc=="10":
                os.system("clear")
                print ("Números amigos")
                        
        elif opc=="11":
                os.system("clear")
                print ("Gracias por utilizarme coomo tu ex")
                print ("Cuidesese, espeo volver a verl@ pronto")        
        else :
                os.system("clear")
                print("Opcion no valida")