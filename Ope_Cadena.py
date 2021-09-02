class Cadena():
    def __init__(self,cadena, cadena2):
        self.cadena=cadena
        self.cadena2=cadena2

    def  recorrerCadena(self):
        for i in self.cadena:
            print(i,'',end='')


    def  buscarCaracter(self,buscado):
        acum=0
        for x,i in enumerate(self.cadena):
            if i== buscado:
                acum=acum+1
        print("Su caracter se encuentra {} veces, dentro de la cadena".format(acum))

    def  listaPosiciones(self,caracter):
        acum=0
        aux=[]
        for x,i in enumerate(self.cadena):
            acum=acum+1
            if i == caracter:
                aux.append(acum)
                lista=aux
            
        print(lista)
    
    def listaPalabras(self): 
       print(self.cadena.split())
    
    def cadenaLista(self):
       print(" , ".join(self.cadena))

    def concatenarCadena(self,nombre):
       print(''.join([self.cadena, self.cadena2]))


cadena= input('')
cad1= Cadena(cadena)
# cad1.recorrerCadena()
# cad1.buscarCaracter('h')
# cad1.listaPosiciones('e')
# cad1.listaPalabras()

# cadena = ['Argentina', 'Uruguay','Ecuador']
# cad1= Cadena(cadena)
# cad1.cadenaLista()

# cadena=input('')
# cadena2=input('')
# cad1 = Cadena(cadena,cadena2)
# cad1.concatenarCadena('')