


#for contador in rangue

##while tambien es una estructura de ciclo
##int es metodo de python quien transforma un dato tipo texto a un dayto de tipo numerico trel o entero
##input es un metodo de python que pide un dato por consola al usuario
condicion=True
while condicion==True:
    numero=int(input('ingrsa el numero ganador :'))
    if numero==10:
        print('ganaste el premio')
        condiciones=False
    else:
        print('ese no es el numero ganador')
##TAREA:
##CREAR UN PROGRAMA QUE ME PIDA MI EDAD, SI INGRESO UNA EDAD INCORRECTA EL PROGRAMA SEGUIRA PIDIENDO MI EDAD
##SI ES LA EDAD CORRECTA ME MOSTRARA UN MENSAJE DE CORRECTO Y SE TERMINA LA EJECUSIONES
condicion=True
while condicion==True:
    edad=int(input('ingresa la edad:'))
    if edad==16:
        print('la edad es correcta')
        condiciones=False
    else:
        print('la edad no es correcta')
