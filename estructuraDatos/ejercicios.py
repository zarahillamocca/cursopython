##Escriba una funcion en python que acepte una lista y genere otra lista eliminando los duplicados numeros.
def delDuplicate(array):
    newArray=[]
    for el in array:
       if el not in newArray:
         newArray.append(el)
    return newArray
arrayD=[1,1,1,2,2,3,3,3,4,4]
print(delDuplicate(arrayD))
##ecriba una funcion que acepte una lista y genere otra con los numeros pares.
def delDuplicate(array):
    newArray=[]
    for el in array:
       if el%2==0 not in newArray:
         newArray.append(el)
    return newArray
arrayD=[1,2,3,4,5,6,7,8,9]
print(delDuplicate(arrayD))
##Escriba una funcion que acepte una lista y genere otra eliminando los duplicados textos.
def stringDuplicate(array):
    newArray=[]
    for i in array:
       if i not in newArray:
         newArray.append(i)
    return newArray
arrayD=["hola","hola","celular","amigo","amigo"]
print(stringDuplicate(arrayD))

#Escribe una funcion que acepte una lista y que genere otra nueva lista  con los numeros primos
