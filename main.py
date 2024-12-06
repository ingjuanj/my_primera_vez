print("hello world")

#and
#True and True  = True
#False and True = False
#True and False = False
#False and False = False

#or 
#True and True  = True
#False and True = True
#True and False = True
#False and False = False

#not
#not True = False
#not False = True

# edad = 0
# edad = input("Digite la edad para solicitar el credito: ")

# if edad==17: 
#     print ("su crédito es como pasante")
# elif edad>=18 and edad<20: 
#     print ("puede solicitar un crédito")
# elif edad>20 and edad<= 24:
#     print ("puede solicitar un créditos con bonificaciones")
# else: 
#     print ("las demas edades no puedes solicitar un credito")

# #Iteraciones

# #ciclo for
# for i in range(1,5):
#     print(f"numero {i+1}")

# for i in ["Cocinar","Programación","Musica","Ingles"]:
#     print(f"Me gusta: {i}")

# #ciclo white
# i=0
# while (i<=5):
#     print(f"hola {i}")
#     i += 1

# while True:
#     numero = int(imput("Ingrese un número: "))

#     if(numero == 10):
#         break

#modular

# def saluda(nombre):
#     pantalla = f"hola compañero {nombre}"
#     return pantalla 

# resultado = saludar("camper")
# print(resultado)


# 06/12/2024 clase de modulización 

from desing.menu import desing
while True:
    opc = desing()
    if opc == 0 : break