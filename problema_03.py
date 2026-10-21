# Función que devuelve un diccionario con k → "nombre_operacion", v → resultado set[int]
def operaciones_conjuntos (lista_01:list[int], lista_02:list[int]) -> dict: 

#   Conjuntos para operar, a partir de las listas
    conjunto_01 = set(lista_01) 
    conjunto_02 = set(lista_02)
    
#   Devolvemos directamente el dict
#   k = nombre_operacion
#   v = set[int] con el resultado
    return {
        "interseccion": conjunto_01 & conjunto_02,
        "union": conjunto_01 | conjunto_02,
        "difrerencia_simetrica": conjunto_01 ^ conjunto_02
    }

# Bloque de prueba
lista_a = [1,5,2,8,2,7,0,4,2]
lista_b = [9,0,6,1,5,3,8,1,2]

resultado = operaciones_conjuntos(lista_a, lista_b)

print(f"intersección: ",resultado["interseccion"])
print(f"unión: ",resultado["union"])
print(f"difrerencia simétrica: ",resultado["difrerencia_simetrica"])