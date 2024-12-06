from logic.formula import hi
def desing():
    print ("Bienvenido al mejor sistema del mundo")
    print ("    0.Atras")
    print ("    1. Desea que muestra maquina saludear")
    opc = int(input("Elige una de las opciones disponibles"))
    if opc ==1:
        name = input("Ingrese su nombre")
        result = hi(name)
        print(result)
    return opc        
