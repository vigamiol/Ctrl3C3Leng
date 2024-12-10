def cargar_indice_desde_archivo(archivo):
    indice = {}
    with open(archivo, "r") as f:
        for linea in f:
            linea = linea.strip()  
            if not linea:  # Ignora líneas vacías
                continue
            try:
                palabra, documentos = linea.split(" ", 1) # Filtrar elementos vacíos y convertir a enteros
                lista_documentos = [int(doc) for doc in documentos.split(",") if doc.strip()]
                indice[palabra] = lista_documentos
            except ValueError:
                print(f"Error procesando la línea: {linea}")
    return indice


def intersectar_listas(listas):
    if len(listas) == 1:              #si solo es una palabra de busqueda se muestra el indice de dicha palabra
        return listas[0]
    return list(set(listas[0]).intersection(intersectar_listas(listas[1:])))



def buscar(indice, consulta):
    terminos = consulta.split()                                              # Dividir la consulta en palabras
    listas_invertidas = [indice.get(termino, []) for termino in terminos]
    if not all(listas_invertidas):                                           # Si alguno de los términos no tiene documentos
        return []                                                            # No hay resultados
    return intersectar_listas(listas_invertidas)

# Cargar el índice desde el archivo
archivo_indice = "lista_invertida_sin_stopwords.txt"  # Cambia esto por tu archivo real
indice = cargar_indice_desde_archivo(archivo_indice)

# Solicitar consultas al usuario
while True:
    consulta = input("Ingresa tu consulta (o escribe 'salir' para terminar): ").strip()
    if consulta.lower() == "salir":
        break
    resultados = buscar(indice, consulta)
    if resultados:
        print(f"Documentos encontrados: {resultados}")
    else:
        print("No se encontraron documentos para la consulta.")
