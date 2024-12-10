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

def remove_lines_with_stopwords(input_filename, output_filename):
    stopwords_found = set()  # Usaremos un set para evitar duplicados de stopwords

    # Procesar el archivo de la lista invertida
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            # Dividir la línea en palabras (esto depende de la estructura del archivo)
            words = line.split()  # Para cada línea, dividimos las palabras por espacios
            
            # Verificar si alguna palabra en la línea es una stopword
            if any(word.lower() in stopwords for word in words):
                stopwords_found.update(word.lower() for word in words if word.lower() in stopwords)
                continue  # Omitir la línea completa si contiene una stopword

            # Escribir la línea en el archivo de salida si no contiene stopwords
            outfile.write(line)

    return stopwords_found

# Usar las funciones para procesar el archivo
input_filename = 'listainvertida.txt'  # Nombre del archivo con la lista invertida
output_filename = 'lista_invertida_sin_stopwords.txt'  # Nombre del archivo de salida

# Llamar a la función para eliminar las líneas con stopwords y mostrar las eliminadas
stopwords_eliminadas = remove_lines_with_stopwords(input_filename, output_filename)

# Mostrar las stopwords que fueron encontradas
print("Stopwords eliminadas:")
print(stopwords_eliminadas)
