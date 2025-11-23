nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

if edad >= 41:
    generacion = "Generación X"
elif edad >= 27:
    generacion = "Generación Milenial"
elif edad >= 13:
    generacion = "Generación Z"
else:
    generacion = "Generación Alfa"

print("Hola", nombre + ", tú perteneces a la", generacion)
