import matplotlib.pyplot as plt

import heapq
import collections

def merge_sort(palavras):
    if len(palavras) <= 1:
        return palavras

    # Divisão da lista de palavras em duas partes
    meio = len(palavras) // 2
    esquerda = merge_sort(palavras[:meio])
    direita = merge_sort(palavras[meio:])
    
    # Junção ordenada das partes
    mesclado = merge(esquerda, direita)
    return mesclado

def merge(esquerda, direita):
    mesclado = []
    i = j = 0
    
    # Combinação ordenada das duas listas
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][1] < direita[j][1] or (esquerda[i][1] == direita[j][1] and esquerda[i][0] <= direita[j][0]):
            mesclado.append(esquerda[i])
            i += 1
        else:
            mesclado.append(direita[j])
            j += 1
    
    # Adição dos elementos restantes da lista esquerda
    while i < len(esquerda):
        mesclado.append(esquerda[i])
        i += 1
    
    # Adição dos elementos restantes da lista direita
    while j < len(direita):
        mesclado.append(direita[j])
        j += 1
    
    return mesclado

def palavras_mais_frequentes(caminho_arquivo, k=50):
    # Leitura do arquivo e contagem das palavras
    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
    
    contador = collections.Counter(palavras)
    frequencia_palavras = [(palavra, frequencia) for palavra, frequencia in contador.items()]
    
    # Ordenação das palavras por frequência utilizando o merge sort
    palavras_ordenadas = merge_sort(frequencia_palavras)
    
    # Seleção das k palavras mais frequentes
    palavras_mais_frequentes = palavras_ordenadas[:k]
    return palavras_mais_frequentes

def resolver_problema_mochila(palavras, pesos, valores, peso_maximo):
    n = len(palavras)
    
    # Criação da tabela para armazenar os resultados
    tabela = [[0] * (peso_maximo + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, peso_maximo + 1):
            if pesos[i - 1] > j:
                # A palavra não pode ser incluída, utiliza-se o valor anterior
                tabela[i][j] = tabela[i - 1][j]
            else:
                # Verifica-se o valor máximo entre incluir a palavra ou não incluir
                tabela[i][j] = max(tabela[i - 1][j], valores[i - 1] + tabela[i - 1][j - pesos[i - 1]])
    
    # Retorna o valor máximo obtido
    return tabela[n][peso_maximo]

# Atribuição de valores e pesos às palavras
palavras = []
pesos = []
valores = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 1, 1, 5, 9, 9, 7, 9, 6, 3, 4, 6, 8, 5, 4, 4, 1, 8, 5, 1, 6, 1, 5, 9, 10, 5, 7, 6, 1, 7, 1, 8, 7, 5, 10]

# Obtendo as palavras mais frequentes
palavras_mais_frequentes = palavras_mais_frequentes('palavras_100k.txt', k=50)

# Atribuindo valores e pesos às palavras
for palavra, _ in palavras_mais_frequentes:
    palavras.append(palavra)
    pesos.append(len(palavra))

# Resolvendo o Problema da Mochila Sem Repetições para diferentes pesos máximos
peso_maximo_lista = range(50, 81)
valores_maximos = []

for peso_maximo in peso_maximo_lista:
    # Resolução do Problema da Mochila para o peso máximo atual
    valor_maximo = resolver_problema_mochila(palavras, pesos, valores, peso_maximo)
    valores_maximos.append(valor_maximo)
    print(f"Peso máximo: {peso_maximo}\tValor máximo: {valor_maximo}")

# Plotando o gráfico
plt.plot(peso_maximo_lista, valores_maximos)
plt.xlabel('Peso Máximo')
plt.ylabel('Valor Máximo')
plt.title('Valores Máximos x Peso Máximo')
plt.show()