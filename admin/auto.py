print(" ")
print("______________________________________________")
print("Automatizando conversion de archivo...")
print("______________________________________________")
print(" ")


archivo = open("pass-phrase/palabras.txt", "r")


linea = archivo.readline()

lista = ""
bandera = 0
contador = 0

print("Leyendo...")

while linea != "":
    if bandera == 1:
        lista += "\n    "
    else:
        lista += "    "
        bandera = 1

    linea = linea.replace("	" , "\" : \"")
    if "\n" in linea:
        linea = linea.replace("\n" , "\",")
    else:
        linea = linea + "\""

    lista += "\"" + linea

    linea = archivo.readline()

archivo.close()

print(" ")
print("Escribiendo...")

archivo = open("pass-phrase\lista_palabras.py", "w")

archivo.write("palabras = {\n")
archivo.write(lista + "\n")
archivo.write("}")
archivo.close()

print(" ")
print(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
print("Automatización completada")
print("Fin del programa")
print(" ")