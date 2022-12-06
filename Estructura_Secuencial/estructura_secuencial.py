#Es aquella en la que una instruccion o accion sigue a otra en secuencia
#se presentan operaciones de inicio a fin, inicializando de variables , operaciones de asignacion
#calculo sumarizacion entre otras
#ejemplo:
#realizar la carga de dos numeros enteros por teclado e imprimir su suma y su producto:
# inicio
# num1
# num2
# suma=num1+num2
# suma, producto
# fin
#Tenemos dos entradas num1 y num2 , dos operadores la suma y el producto de los valores ingresados y os salidas
#que son el resultado de la suma y el producto de los valores ingresados .
#En el simbolo de la impresion podemos ingresar uno o mas salidas , eso que a criterio del programador , lo mismo para indicar la s entradas por el teclado.
#Mostrar por consola cuantas vocales "a" tiene el mensaje
mensaje =(input("ingrese un mensaje"))
contador=0
for letras in mensaje:
    if letras=="a":
        contador +=1
print("este mensaje tiene", contador,"a")