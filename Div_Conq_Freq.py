import time
from collections import Counter

def merge_sort(palavras):
    if len(palavras) <= 1:
        return palavras

    mid = len(palavras) // 2
    left = merge_sort(palavras[:mid])
    right = merge_sort(palavras[mid:])
    
    merged = merge(left, right)
    return merged

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1] or (left[i][1] == right[j][1] and left[i][0] <= right[j][0]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

with open('palavras_100k.txt', 'r') as file:
    conteudo = file.read()
    palavras = conteudo.split()

contador = Counter(palavras)
start_time = time.time()
frequencia_palavras = merge_sort(list(contador.items()))

with open('final_Freq.txt', 'w') as output_file:
    for word, count in frequencia_palavras:
        for _ in range(count):
            print(word, file=output_file)

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time 100k: {execution_time:.2f} seconds")
