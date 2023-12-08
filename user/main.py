import random
from lista_palabras import palabras

print("-----------------------------")
print(" Pass maker")
print("-----------------------------")
print(" ")

bandera = 0
while bandera == 0:
    try:
        repeticiones = int(input("Ingrese la cantidad de palabras que quiere generar: "))
        bandera = 1
    except:
        print("- Recuerde que debe ser un número -")

bandera = 0
while bandera == 0:
    numeros = input("Quiere usar numeros? (s/n): ").lower()
    if "s" == numeros:
        bandera = 1
    elif "n" == numeros:
        bandera = 1

pass_phrase = ""

if numeros == "s":
    for repeticion in range(1, (repeticiones + 1)):
        combinacion = ""
        for numero in range(1, 6):
            valor = random.randint(1, 6)
            combinacion += str(valor)

        if repeticion < repeticiones:
            pass_phrase += palabras[combinacion] + str(random.randint(0,99)) + "-"
        else:
            pass_phrase += palabras[combinacion] + str(random.randint(0,99))
else:
    for repeticion in range(1, (repeticiones + 1)):
        combinacion = ""
        for numero in range(1, 6):
            valor = random.randint(1, 6)
            combinacion += str(valor)

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