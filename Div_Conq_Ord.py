import time

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
        if left[i].lower() < right[j].lower():
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

with open('palavras_100k.txt', 'r') as f:
    conteudo = f.read()
    palavras = conteudo.split()

start_time = time.time()

palavras_total = merge_sort(palavras)

with open('final_Ord.txt', 'w') as output_file:
    for palavra in palavras_total:
        print(palavra, file=output_file)

end_time = time.time()
execution_time = end_time - start_time

minutes = int(execution_time // 60)
seconds = int(execution_time % 60)
print(f"Execution time 100k: {execution_time:.2f} seconds")
