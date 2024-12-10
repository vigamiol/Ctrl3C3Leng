stopwords = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself",
    "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
    "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in",
    "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor",
    "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should",
    "now", "d", "ll", "m", "o", "re", "ve", "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn",
    "haven", "isn", "ma", "mightn", "mustn", "needn", "needn", "hadn", "shouldn", "wasn", "weren", "won"
])

def remover_stopwords(texto):
    palabras = texto.lower().split()  # Convertir el texto a minúsculas y dividir por espacios
    palabras_filtradas = [palabra for palabra in palabras if palabra not in stopwords]  # Filtrar las stopwords
    palabras_removidas = [palabra for palabra in palabras if palabra in stopwords]  # Las stopwords eliminadas
    return " ".join(palabras_filtradas), palabras_removidas  # Devolver las palabras filtradas y las eliminadas

# Leer el archivo con la lista invertida
archivo_entrada = 'texto_certamen.txt'  # Nombre de tu archivo

# Procesar el archivo
with open(archivo_entrada, 'r') as archivo:
    for linea in archivo:
        # Eliminar las stopwords de cada línea y obtener las stopwords eliminadas
        linea_limpia, palabras_removidas = remover_stopwords(linea)

        # Mostrar las stopwords eliminadas
        if palabras_removidas:
            print(f'Stopwords eliminadas en la línea: {", ".join(palabras_removidas)}')
        else:
            print("no se elimino ninguna Stopwords en esta linea")