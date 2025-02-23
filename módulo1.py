notas = []

while True:
    string = input("Ingrese una lista de numeros separados por espacios entre 1 y 20 (o salir para terminar): ")

    if string.lower() == "salir":
        break
    for nota in string.split():
     try:
        nota = int(nota)
        if 0 <= nota <= 20:
            notas.append(nota)
        else:
             print("La nota",nota,"no esta entre 0 y 20. Se ignora")
     except ValueError:
        print(nota,"no es un numero valido, se omitira")

if notas:
    promedio = sum(notas) / len(notas)
    print("\nLa lista de notas es:", notas)
    print("\nEl promedio de las notas es: {:.2f}".format(promedio))
else:
    print("No se ingresaron notas validas.")