##averiguar sobre funciones
##Es un grupo de instrucciones que constituyen una unidad logica
##del programa y resuelve un programa muy concreto , tienen un doble objetivo:
##Dividir y organaizar el codigo en partes mas sencillas.
##Encapsular el codigo que se repite a lo largo de un programa para ser reutilizado.
##SINTAXIS:
##La palabra clave def
##Un nobre de funcion
##Prentesis() y dentro de los parentesisi los parameyros de entrada aunque los parametros de entrada sean opcionales
##dos puntos":"
##Algun bloque de codigo ´para ejecutar
##Una sentencia de retorno
##2 tipos de funciones
##funciones propias de python
print()##sirve para mostrar mensaje o resultado
int()##sirve para convertir String en entero
input()##esta funcion sirve para pedir datos al usuario
##todo lo que se ingrese en imput sera tomado como texto
##funciones creadas:
##estructura para crear funciones
def saludo(a,b)
    resultadodo=a+b
    return resultado
##uso de funcion
print(saludo(4,6))
numero=10 #10
int(numero) #10
#int es el nombre de la funciones
#()y dentro de los parantesis van los parametros
#parametros
def countVocales(texto):
    vocales=["a","e","i","o","u"]
    contadorVocales=0
    for letras in texto:
        if letras in vocales:
            contadorVocales+=1
    return contadorVocales
#TAREA:
#crear una funcion de operaciones matematicas
def operadorMatematico(numero1,numero2,operacion):
    if operacion=="suma":
        operadorMatematico="la suma de: ",numero1,"+",numero2,"es",numero1+numero2
    elif operacion=="resta":
        operadorMatematico = "la resta de: ", numero1, "-", numero2, "es", numero1 - numero2
    elif operacion == "multiplicacion":
        operadorMatematico = "la multiplicacion de: ", numero1, "*", numero2, "es", numero1 * numero2
    elif operacion == "divicion":
        operadorMatematico = "la divicion de: ", numero1, "/", numero2, "es", numero1 / numero2
    return operadorMatematico
print(operadorMatematico(10,12,"suma"))

#si noperacion!=suma resta multiplicacion divicion
def mensaje(nombre,apellido,accion):
    if accion== "saludo":
        mensaje="hola",nombre,apellido,"como estas"
    elif accion == "despedida":
        mensaje="adios",nombre,apellido
    return mensaje
print(mensaje("jose","alvarez","saludo"))
##vocales en una oracion
sentence=input("enter sentence: ")
vocales=["a","e","i","o","u"]
def countvocal(oracion,vocal):
    contador=0
    for word in oracion:
        if word in vocal:
            contador+=1
    return contador
print(countvocal(sentence,vocales))
















