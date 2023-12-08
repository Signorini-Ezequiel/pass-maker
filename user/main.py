from lista_palabras import palabras
import secrets

print("-----------------------------")
print(" Pass maker")
print("-----------------------------")
print(" ")

bandera = 0
while bandera == 0:
    try:
        cantidad = int(input("Ingrese la cantidad de palabras que quiere generar: "))
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
    for repeticion in range(1, (cantidad + 1)):
        if repeticion < cantidad:
            if(1 == secrets.randbelow(2)):
                pass_phrase += palabras[secrets.randbelow(7775)] + str(secrets.randbelow(999)) + "-"
            else:
                pass_phrase +=  str(secrets.randbelow(999)) + palabras[secrets.randbelow(7775)] + "-"
        else:
            if(2 == secrets.randbelow(2)):
                pass_phrase += palabras[secrets.randbelow(7775)]
            else:
                pass_phrase += palabras[secrets.randbelow(7775)] + str(secrets.randbelow(999))
else:
    for repeticion in range(1, (cantidad + 1)):

        if repeticion < cantidad:
            pass_phrase += palabras[secrets.randbelow(7775)] + "-"
        else:
            pass_phrase += palabras[secrets.randbelow(7775)]

print(" ")
print(f"La pass-phrase es: {pass_phrase}")

print(" ")
print("-----------------------------")
print("Fin del programa")
print(" ")