print(" ")
print("______________________________________________")
print("Automatizando conversion de archivo...")
print("______________________________________________")
print(" ")


archivo = open("./admin/palabras.txt", "r")


linea = archivo.readline()

lista = ""
bandera = 0

print("Leyendo...")

while linea != "":
    if bandera == 1:
        lista += "\n    "
    else:
        lista += "    "
        bandera = 1

    
    if "\n" in linea:
        linea = linea.replace("\n" , "\",")
    else:
        linea = linea + "\""

    linea = linea.strip().split("	")
    lista += "\"" + linea[1]

    linea = archivo.readline()

archivo.close()

print(" ")
print("Escribiendo...")

archivo = open("./user/lista_palabras.py", "w")

archivo.write("palabras = [\n")
archivo.write(lista + "\n")
archivo.write("]")
archivo.close()

print(" ")
print(". . . . . . . . . . . . . . . . . . . . . . . . . . .")
print("Automatización completada")
print("Fin del programa")
print(" ")