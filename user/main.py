import random
from lista_palabras import palabras

print("-----------------------------")
print(" Pass Helper")
print("-----------------------------")
print(" ")

bandera = 0
while bandera == 0:
    try:
        repeticiones = int(input("Ingrese la cantidad de palabras que quiere generar: "))
        bandera = 1
    except:
        print("- Recuerde que debe ser un número -")

pass_phrase = ""

print(" ")

for repeticion in range(1, (repeticiones + 1)):
    combinacion = ""
    for numero in range(1, 6):
        valor = random.randint(1, 6)
        combinacion += str(valor)
    print(f"La palabra {repeticion} es: \"{palabras[combinacion]}\" y corresponde al valor: {combinacion}")

    if repeticion < repeticiones:
        pass_phrase += palabras[combinacion] + "-"
    else:
        pass_phrase += palabras[combinacion]

print(" ")
print(f"La pass-phrase es: {pass_phrase}")

print(" ")
print("-----------------------------")
print("Fin del programa")
print(" ")