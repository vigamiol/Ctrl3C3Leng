def cargar_indice_desde_archivo(archivo):
    """
    Carga el índice invertido desde un archivo de texto.
    Maneja casos donde las listas de documentos tienen comas adicionales o están vacías.
    """
    indice = {}
    with open(archivo, "r") as f:
        for linea in f:
            linea = linea.strip()  # Quita espacios en blanco al inicio y al final
            if not linea:  # Ignora líneas vacías
                continue
            try:
                palabra, documentos = linea.split(" ", 1)
                # Filtrar elementos vacíos y convertir a enteros
                lista_documentos = [int(doc) for doc in documentos.split(",") if doc.strip()]
                indice[palabra] = lista_documentos
            except ValueError:
                print(f"Error procesando la línea: {linea}")
    return indice

def intersectar_listas(listas):
    """
    Realiza la intersección recursiva de múltiples listas.
    """
    if len(listas) == 1:
        return listas[0]
    return list(set(listas[0]).intersection(intersectar_listas(listas[1:])))

def buscar(indice, consulta):
    """
    Realiza una búsqueda en el índice para los términos de la consulta.
    Devuelve los documentos que contienen todos los términos.
    """
    terminos = consulta.split()  # Dividir la consulta en palabras
    listas_invertidas = [indice.get(termino, []) for termino in terminos]
    if not all(listas_invertidas):  # Si alguno de los términos no tiene documentos
        return []  # No hay resultados
    return intersectar_listas(listas_invertidas)

def procesar_consultas(input_txt, output_txt, indice):
    """
    Lee consultas desde un archivo de entrada, realiza búsquedas y guarda los resultados en un archivo de salida.
    """
    with open(input_txt, "r") as f_in, open(output_txt, "w") as f_out:
        for linea in f_in:
            consulta = linea.strip()  # Lee la consulta
            if not consulta:
                continue
            resultados = buscar(indice, consulta)
            # Escribir los resultados al archivo de salida
            f_out.write(f"Consulta: {consulta} -> Resultados: {resultados}\n")
    print(f"Resultados almacenados en {output_txt}")

# Configurar los archivos
archivo_indice = "lista_invertida_sin_stopwords.txt"  # Archivo con el índice invertido
archivo_consultas = "archivo_consultas.txt"     # Archivo con las consultas (tres palabras por línea)
archivo_resultados = "resultados.txt"   # Archivo donde se almacenan los resultados

# Cargar el índice y procesar consultas
indice = cargar_indice_desde_archivo(archivo_indice)
procesar_consultas(archivo_consultas, archivo_resultados, indice)