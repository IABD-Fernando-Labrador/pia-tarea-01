# Problema 2. Frecuencia de palabras en un texto.

import string

# cuenta_palabras(lista: list[int], ruta: str) -> dict

#   Sólo para ficheros pequeños. El método read() lee todas las líneas del texto
#   ---------------------------------------------------------------------------------
#   1) La eliminación de los signos de puntuación require una "tabla de traducción".
#   2) Construimos una cosntante con símbolos. Añadimos otros símbolos y dígitos.
#   3) Abrimos el archivo almacenando en una única cadena el texto en minúsculas.
#   4) Separamos las palabras.
#   5) Elaboramos el dict con las frecuencias.
#   ---------------------------------------------------------------------------------

def cuenta_palabras(lista: list[int], ruta: str) -> dict:
    
    PUNTUACION_ES = string.punctuation + string.digits + "¿¡"   # Puntuación estandar + dígitos y puntuación en español
    tabla_traduccion = str.maketrans("","", PUNTUACION_ES)      # Tabla de traducción: "" → sin argumentos = eliminar

    with open(ruta,"r",encoding="utf-8") as fichero:            # Abrimos el fichero en un único stream
        texto = fichero.read().lower()                          # y lo conviertiemos a minúscula
        
    texto = texto.translate(tabla_traduccion)                   # Aplicamos la tabla, eliminando los caracteres
    
    palabras_texto = texto.split()                              # Separamos las palabras en un list[str]
    
    frecuencias = {palabra.lower(): 0 for palabra in lista}     # Iniciamos el diccionario de frecuencias: k=palabra, apariciones v=0

    for palabra in palabras_texto:                              # Bucle de conteo
        if palabra in frecuencias:
            frecuencias[palabra] +=1
    
    return frecuencias

# Prueba:
# -------
lista_palabras = ["menor", "o", "palabra", "de", "para", "por", "a", "con", "python", "todo", "en", "sin", "problema", "y"]

resultado = cuenta_palabras(lista_palabras,"problema_02.txt")

for palabra in sorted(resultado):
    print(f"{palabra}: {resultado[palabra]}")