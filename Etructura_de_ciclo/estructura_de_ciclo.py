


#for contador in rangue

##(while tambien es una estructura de ciclo
##int es metodo de python quien transforma un dato tipo texto a un dayto de tipo numerico trel o entero
##input es un metodo de python que pide un dato por consola al usuario
##condicion=True
##while condicion==True:
   ## numero=int(input('ingrsa el numero ganador :'))
   ## if numero==10:
       ## print('ganaste el premio')
        ##condiciones=False
   ## else:
    ##    print('ese no es el numero ganador')
##TAREA:
##CREAR UN PROGRAMA QUE ME PIDA MI EDAD, SI INGRESO UNA EDAD INCORRECTA EL PROGRAMA SEGUIRA PIDIENDO MI EDAD
##SI ES LA EDAD CORRECTA ME MOSTRARA UN MENSAJE DE CORRECTO Y SE TERMINA LA EJECUSIONES
##condicion=True
#while condicion==True:
 ##   edad=int(input('ingresa la edad:'))
 ##   if edad==16:
  ##      print('la edad es correcta')
  ##      condiciones=False
  ##  else:
  ##      print('la edad no es correcta')
##
##password='72884335'
##for intentos in range(1,4):
##    print('este es tu',intentos,'intento')
##    newpassword=input("ingresa el password correcto:")
##    if newpassword==password:
##        print("bienvenidos al sistema joven")
##        break
##    else:
##        print("password incorrecto sigue intentando")
##
##condicion=True
##eval=1
##while condicion==True:
##    if eval==5:
##        print("estamos en 5")
##        condicion=False
##    else:
##        print(eval)
##       eval+=1
##tabla de multiplicar
##mostrar la tabla del numero que quieras
##numero=int(input("ingrese un numero npara mostrar la tabla qhe quiere visualizar"))
##for numeros in range(1,11):
##    print(numeros,"*",numero,"=",numero*numero)
##evaluando:
##eval=True
#while eval==True:
#    numero=int(input('ingrese un numero para mostrar la tabla he quiere visualizar:'))
#    if numero==0:
#        print("error saliendo del programa")
#        break
#    else:
#        for numeros in range(1, 11):
#            print(numeros, "*", numero,"=",numero * numero)

#mensaje ="hola"
#print(mensaje[3])
#for letra in mensaje:
#    print(letra)
#ingresarv un mensaje que
#mostrar por consola cuantas vocales "a"
#tiene el mensaje


#mensajes =input("ingrese un mensaje")
#contador=0
#for letras in mensajes:
#    if letras=="a":
#      contador+=1
#print("en este mensaje tienes",contador,"letras a")
##numeros primos la divicion en ellos mismos y 1 residuo es simpre cero
#2/1==0
#2/2==0
#3/1==0
#3/3==0
#5/1==0
#5/5==0
##hacer un algoritmo que pida al usuario un numero
##y me diga si es num ero primo o no
#numero=int(input("ingrese un numero"))
#for n in range(2,numero):
#    if numero%n ==0:
#        break
#    else:
#        print("es primo")
#        break
#        print("no es primo")

condicion=True
while condicion==True:
    numero=int(input("ingrese un numero"))
    if numero%2==0 or numero%3 ==0:
        print("no es primo")
    else:
        print("es primo")
        condicion=False

#Escribir un programa que muestre el eco de
# etodo lo que el usuario introduzca hasta que el usurio escriba "
#"salir"que terminara
palabra=""
while palabra!="salir":
    palabra= input("escriba algo:")
    print(palabra)

#pedir un texto largo y mostrar contar la cantidad de vocales que existe en el texto
oracion =input("ingrese su oracion")
vocales=["a","e","i","o","u"]
contadorVocales=0
for letras in oracion:
    if letras in vocales:
        contadorVocales+=1
    print("la cantidad de vocales es:",contadorVocales)
#2
sentence=input("ingrese una oracion")
countVocals=0
for words in sentence:
    match words:
     case "a":
         countVocals+=1
     case "e":
         countVocals+=1
     case "i":
         countVocals+=1
     case "o":
         countVocals+=1
     case "u":
         countVocals+=1
print("la cxantidad de vocales es:",countVocals)

















