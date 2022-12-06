#definir una funcion max() que tome como argumento un array de numeros y devuelcva el mayor del array.
def mayor(6,9):
    if (6>9):
        return 6
    if (6>9):
        return 9
print(mayor)
#Escribe una funcion que almacene en una lista los siguientes precios 50,75,46,22,80,65,8, y mustre por pantalla enl mayor y menor  de los precios
precio= [50, 75, 46, 22, 80, 65, 8]
mayor = menor = precio[0]
for precio in precio:
    if precio < menor:
        menor = precio
    elif precio > mayor:
        mayor = precio
print("El prcio menor es " + str(menor))
print("El precio mayor es " + str(mayor))
#escribe una funcion mas larga () que tome un array de palabras y devuelva la mas larga
def mas_larga(lista):
    palabra_mayor = len(lista[0])
    palabra_mostrar = lista[0]
    for palabra in lista:
        if palabra_mayor <= len(palabra):
            palabra_mostrar = palabra
            palabra_mayor = len(palabra)
        else:
            palabra_mostrar = palabra_mostrar
    print(palabra_mostrar)
lista = ["zarahi", "llamocca",]
mas_larga(lista)


.

