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
