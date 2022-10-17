##
##operador foca
##texto="hola mundo"
##print(texto[5:])
##tendremos una variable con el mensaje hola mundo  =texto=imput=para pedir texto

##pedimos al usuario un texto
##si el texto ingresado es hola
##mostraras el mensaje completo
##si el texto ingresado es como estas
##extraeras el mensaje la palabra hola
##si el texto ingresado es saludo
##extraeras del mensaje la palabra mundo
##si se ingresa otro texto
##mostraras por defecto el mensaj de error
##mensaje="hola mundo"
##texto=input("ingresa un texto:")
##match texto:
##    case "hola":
##        print(mensaje[:])
##    case"como estas":
##        print(mensaje[:4])
##case "saludo":
##     print(mensaje[5:])
##   case _:
##        print("error")
## convirtiendo match a if
mensaje="hola mundo"
texto=input("ingresa un texto:")
if texto:
    if texto=="hola":
        print(mensaje[:])
    elif texto=="como estas":
        print(mensaje[:4])
    elif texto=="saludo":
        print("mensaje[5:]")
    else:
        print("error")



