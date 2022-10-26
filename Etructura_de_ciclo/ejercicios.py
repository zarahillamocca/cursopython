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
print(operadorMatematico(10, 12, "suma"))






