# Problema 1. Procesamiento de una lista de enteros.

lista = [4, -1, 2, 4, 3, -5, 2]

resultado = []  # lista con los resultados
vistos = set()  # conjunto para obtener los elementos únicos

# Resultado en una nueva lista
for n in lista:
    if n>=0 and not n in vistos:
        vistos.add(n)
        resultado.append(n)

resultado.sort()

print(f"resultado: ", resultado)