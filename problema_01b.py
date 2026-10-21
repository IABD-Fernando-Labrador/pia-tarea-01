# Problema 1b. Procesamiento de una lista de enteros.
# Alternativa usando la lista inicial

lista = [4, -1, 2, 4, 3, -5, 2]

vistos = set()

lista = [
    n
    for n in lista
    if n>=0 and not (n in vistos or vistos.add(n))
]

lista.sort()

print(f"resultado: ", lista)

# Cómo evaluamos si el elemento de la lista es positivo y no está repetido
#
# if n>=0 and not (n in vistos or vistos.add(n))
# ----------------------------------------------
#
# Utilizamos la propiedad bool(None) = False
#   - Si (n in vistos) = True, no evalúa el segunda término de la expresión 
#     n → EXCLUIDO
#
#   - Si (n in vistos) = False, añade n al set devolviendo None
#     El resultado not(False or None) = true 
#     n → INCLUIDO en list[]
