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

##Operador Matematico(NumeroUno,NumeroDos,Operacion)

##Opercion Matematica (4,5"suma")
##Por Consola La SUma  De 4+5
##1 UTILIZAR LA PALABRA SERVADA DEF
##2 ASIGNAMOS UN NOMBRE A LA FUNCION--DESCRIPTIVO
##3 SIEMPRE TIENE QUE RECIVIR PARAMETROS
 ##()--No Resive Parametros
 ##(Nombre)---la funcion esta reciviendo parametros
 ##(edad,nombre)
##4 SIEMPTRE la funcion tiene que retornar un tipo de dato
def saludo(nombre):
    respuesta=f"hola como estas nombre"
    return respuesta
##como uso
arrayAmigos=["ronald","claudio","jose","diego","mozar","kevin","lilian"]
for amigo in range(0,len(arrayAmigos)):
    print(saludo(arrayAmigos[amigo]))

##CREAR UNA FUNCION QUE ME RETORNE N NUMEROS FIBONACI
operacion="resta"
numeroUno=80
numeroDos=50
if operacion=="suma"
    print
## aqui crear mis funciones
def operaciones(num1,num2,operador):+
    if operador=="suma":
        total=num1+num2
    if operador=="resta":
        total=num1-num2
    if operador=="por":
        total=num1*num2
    if operador=="entre":
        total=num1/num2
    return total
def sludo():
    mensaje="hola alumnitos bellos"
    return mensaje
















