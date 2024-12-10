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

def remove_stopwords(text):
    words = text.lower().split()  # Convertir el texto a minúsculas y dividir por espacios
    filtered_words = [word for word in words if word not in stopwords]  # Filtrar las stopwords
    stopwords_removed = [word for word in words if word in stopwords]  # Las stopwords eliminadas
    return " ".join(filtered_words), stopwords_removed  # Devolver las palabras filtradas y las eliminadas

# Leer el archivo con la lista invertida
input_filename = 'texto_certamen.txt'  # Nombre de tu archivo

# Procesar el archivo
with open(input_filename, 'r') as infile:
    for line in infile:
        # Eliminar las stopwords de cada línea y obtener las stopwords eliminadas
        clean_line, stopwords_removed = remove_stopwords(line)

        # Mostrar las stopwords eliminadas
        if stopwords_removed:
            print(f'Stopwords eliminadas en la línea: {", ".join(stopwords_removed)}')
        else:
            print("no se elimino ninguna Stopwords en esta linea")