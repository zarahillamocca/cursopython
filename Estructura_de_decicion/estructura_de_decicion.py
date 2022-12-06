#Estructura de decicion
#if realiza una accion especificada solo cuando la condicion es veerdadera; de lo conrario la accion se ignora
#La estructura if / else permite al programador especificar que una accion diferente se debe desarrollar cuando la condicion es falsa.
#por ejemplo, la sentencia en pseudocodigo:si el estudiante obtiene una nota igual o superior a 16:
#entonces: aprovado
#si no: suspendido
if nota >= 16:
    print("aprovado")
else:
    print("Suspendido")
#Tambien se utiliza la estructura de seleccion multiple if/elif/else/:
if nota >= 16:
    print("A")
elif nota >= 15:
    print("B")
elif nota >= 14:
    print("c")
elif nota >= 13:
    print("D")
else:
    print("F")
##operador match
operacion="suma"
match operacion:
    case "suma":
        print("realizare una suma")
    case "resta":
        print("realizare una resta")
    case "multiolicacion":
        print("realizare una multiplicacion")
    case _:
        print("no hay operacion")

#tendremos una variable con el mensaje hola mundo,pedimos al usuario un texto,
#si el texto ingresado es hola,mostraras un mensaje completo
# si el texto ingresado es como estas, extraeras del mensaje la palabra hola
#si el texto ingresado es saludo, extraeras del mensaje la palabra mundo
#si se ingresa otro texto ,mostrara por defecto el mensaje de error
mensaje="hola mundo"
texto=input("ingrsa un texto")
match texto:
    case "hola":
        print(mensaje[:])
    case "como estas":
        print(mensaje[:4])
    case "saludo":
        print(mensaje[5:])
    case _:
        print("error")


#convirtiendo match a if
mensaje="hola mundo"
texto=input("ingresa texto")
if texto:
    if texto=="hola":
        print(mensaje[:])
    elif texto=="como estas":
        print(mensaje[:4])
    elif texto=="saludo":
        print(mensaje[5:])
    else:
        print("error")