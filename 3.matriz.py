# S12 - Clase Virtual (2021-08-20)
# S13 - Clase Virtual (2021-08-23)
#S13 - Clase Virtual (2021-08-27)
import os
class Matriz:
    def __init__(self,matriz,fila,col):
        self.matriz = matriz
        self.fila=fila
        self.col = col
        
    def ingresar(self):
        self.matriz = []
        for fila in range(self.fila):
            columnas=[]
            os.system("cls")
            for col in range(self.col):
                valor=int(input("Fila[{}] col[{}]: ".format(fila,col)))
                columnas.append(valor)
            self.matriz.append(columnas)
            
        
    def presentar(self):
        #os.system("cls")
        print("________")
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print() 
        print("________")
    
    def buscar (self,valor):
        enc = {}
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col] == (valor):
                    enc["fila"]=fila
                    enc["col"]=col
                    break
            if enc: break
                
        return enc
    
    def buscarw (self,valor):
        enc = {}
        fila=0
        band=True
        while fila < len(self.matriz)and band:
            col=0
            while col < len(self.matriz[fila]) and band:
                if self.matriz[fila][col] == str (valor):
                    enc["fila"]=fila
                    enc["col"]=col
                    band=False
                else: col += 1
            fila += 1
        return enc
    
    def sumar (self,matriz2):
        matrizsuma = []
        for fila in range(self.fila):
            columnas=[]
            for col in range(self.col):
                valor= self.matriz[fila][col] + matriz2[fila][col]
                columnas.append(valor)
            matrizsuma.append(columnas)
        return matrizsuma
   
        
        
#numeros = [[10,20,30],[60,80,90],[25,35,55]]
numeros = []
# col = numeros[0]
# print(numeros[0],numeros[0][1])
# print(col,col[1])
mat1 = Matriz(numeros,2,2)
mat2 = Matriz(numeros,2,2)
mat1.ingresar()
mat2.ingresar()
mat1.presentar()
mat2.presentar()
print(mat1.sumar(mat2.matriz))
# mat.ingresar()
# print(mat.buscar(8))
#resp= mat.buscar(30)
#if resp: print("El valor se encuentra en las siguientes coordenadas",resp)
#else: print("no esxiste el valor en la matriz")