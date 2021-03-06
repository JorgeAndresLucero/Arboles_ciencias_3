from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)

pila = Pila()
 
#lectura del archivo
fo = open("expresiones.in","r")
lineas  = (fo.read().splitlines())
fo = open("expresiones.out","a")
for i in lineas:
    convertir(i.split(" "),pila)
    resultado = evaluar(pila.desapilar())
    print("{} = {} ".format(i,resultado))
    #Guardar resultado en el archivo
    fo.write(str(resultado)+"\n")
fo.close()
fo.close()
