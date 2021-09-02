class Menu:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elija opcion[1...{}]: ". format(len(self.opciones)))
        return opc
    
opc =""   
while opc !="5":
    men = Menu("Menu principal",["1) Calculadora","2) Numeros","3) Listas","4) Cadenas","5) Salir"]) 
    opc = men.menu()
    if opc == "1":
        opc1 =""
        while opc1 !="10":
            men1 = Menu("Menu Calculadora",["1) Suma","2) Resta","3) Multiplicacion","4) Division","5) Exponente","6) Valor absoluto","7) Circunferencia","8) Area circulo","9) Area cuadrado","10) Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
               print("suma de dos numeros")
               n1 = int(input("ingresenumero1: "))
               n2 = int(input("ingrese numero2: "))
               print(n1+n2)
        
            elif opc1 == "2":
                    print("resta de dos numeros")     
                    n1 = int(input("ingresenumero1: "))
                    n2 = int(input("ingrese numero2: "))
                    print(n1-n2) 
                
            elif opc1 == "3":
                    print("multiplicacion de dos numeros")
                    n1 = int(input("ingresenumero1: "))
                    n2 = int(input("ingrese numero2: "))
                    print(n1*n2)
        
            elif opc1 == "4":
                    print("division de dos numeros")
                    n1 = int(input("ingresenumero1: "))
                    n2 = int(input("ingrese numero2: "))
                    print(n1/n2)
            
            elif opc1 == "5":
                    print("Calcular exponente")
                    base=int(input("ingrese la base"))    
                    exponente= int(input("ingrese el exponente"))
                    def potencia(base, exponente):
                       resultado= 1
                       for i in range (exponente):
                           resultado *= base
                           return resultado
                    print(base**exponente)
                
            elif opc1 == "6":
                    print("Calcular el valor absoluto")
                    absoluto= int(input("ingrese un valor"))
                    print(abs(absoluto))
                         
            elif opc1 == "7":
                    print("calcular circunferencia")
                    from math import pi
                    radio = float(input("Ingrese el valor del radio: "))
                    circunferencia = 2 * pi * radio
                    print("La circunferencia del circulo es igual a{:.2f}".format(circunferencia))
            
            elif opc1 == "8":
                    print("calcular area de un circulo")
                    from math import pi
                    radio = float(input("Ingrese el valor del radio: "))
                    area = pi * radio ** 2
                    print("El area del circulo es igual a{:.2f}".format(area))
            
            elif opc1 == "9":
                    print("calcular area de un cuadrado")
                    lado = int(input("ingrese la medida del lado del cuadrado: "))
                    area = lado* lado
                    print("El area del cuadrado es: ", area)
            
            elif opc1 == "10":
                    print("GRACIAS POR USAR NUESTRO SISTEMA ")
                    
            else:
                print("Opcion no valida ")
            
print("VUELVA PRONTO")    