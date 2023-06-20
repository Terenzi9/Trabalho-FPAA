import matplotlib.pyplot as plt

import heapq
import collections

def merge_sort(palavras):
    if len(palavras) <= 1:
        return palavras

    meio = len(palavras) // 2
    esquerda = merge_sort(palavras[:meio])
    direita = merge_sort(palavras[meio:])
    
    mesclado = merge(esquerda, direita)
    return mesclado

def merge(esquerda, direita):
    mesclado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][1] < direita[j][1] or (esquerda[i][1] == direita[j][1] and esquerda[i][0] <= direita[j][0]):
            mesclado.append(esquerda[i])
            i += 1
        else:
            mesclado.append(direita[j])
            j += 1
    
    while i < len(esquerda):
        mesclado.append(esquerda[i])
        i += 1
    
    while j < len(direita):
        mesclado.append(direita[j])
        j += 1
    
    return mesclado

def palavras_mais_frequentes(caminho_arquivo, k=50):
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
    
    contador = collections.Counter(palavras)
    frequencia_palavras = [(palavra, frequencia) for palavra, frequencia in contador.items()]
    
    palavras_ordenadas = merge_sort(frequencia_palavras)
    
    palavras_mais_frequentes = palavras_ordenadas[:k]
    return palavras_mais_frequentes

def resolver_problema_mochila(palavras, pesos, valores, peso_maximo):
    n = len(palavras)
    
    tabela = [[0] * (peso_maximo + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, peso_maximo + 1):
            if pesos[i - 1] > j:
                tabela[i][j] = tabela[i - 1][j]
            else:
                tabela[i][j] = max(tabela[i - 1][j], valores[i - 1] + tabela[i - 1][j - pesos[i - 1]])
    
    
    return tabela[n][peso_maximo]


palavras = []
pesos = []
valores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 1, 1, 5, 9, 9, 7, 9, 6, 3, 4, 6, 8, 5, 4, 4, 1, 8, 5, 1, 6, 1, 5, 9, 10, 5, 7, 6, 1, 7, 1, 8, 7, 5, 10]


palavras_mais_frequentes = palavras_mais_frequentes('palavras_100k.txt', k=50)


for palavra, _ in palavras_mais_frequentes:
    palavras.append(palavra)
    pesos.append(len(palavra))


peso_maximo_lista = range(50, 81)
valores_maximos = []

for peso_maximo in peso_maximo_lista:
    valor_maximo = resolver_problema_mochila(palavras, pesos, valores, peso_maximo)
    valores_maximos.append(valor_maximo)
    print(f"Peso máximo: {peso_maximo}\tValor máximo: {valor_maximo}")

# Plotando o gráfico
plt.plot(peso_maximo_lista, valores_maximos)
plt.xlabel('Peso Máximo')
plt.ylabel('Valor Máximo')
plt.title('Valores Máximos x Peso Máximo')
plt.show()