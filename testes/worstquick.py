import time
import random
import pandas as pd
import os

def quicksort(v, inicio, fim):
    if inicio < fim:
        p = particao(v, inicio, fim)
        quicksort(v, inicio, p - 1)
        quicksort(v, p + 1, fim)

def particao(v, inicio, fim):
    pivot = v[inicio]
    indice = fim

    for i in range(fim, inicio, -1):
        if v[i] <= pivot:
            v[i], v[indice] = v[indice], v[i]
            indice -= 1

    v[inicio], v[indice] = v[indice], v[inicio]
    return indice

def kth_smallest_quick(v, k):
    inicio, fim = 0, len(v) - 1
    while inicio <= fim:
        p = particao(v, inicio, fim)
        if p == k:
            return v[p]
        elif p < k:
            inicio = p + 1
        else:
            fim = p - 1

def verificar_ordem(lista):
    if lista == sorted(lista):
        return 'Ordenada'
    elif lista == sorted(lista, reverse=True):
        return 'Ordenada ao contrário'
    else:
        return 'Desordenada'

def executar_experimentos(tamanhos_listas, num_repeticoes=10):
    resultados = []

    for tamanho in tamanhos_listas:
        tempos_execucao = []

        for _ in range(num_repeticoes):
            random.seed()

            lista = list(range(tamanho, 0, -1))

            k = tamanho // 2

            ordem_lista = verificar_ordem(lista)

            start_time = time.perf_counter()
            kth_smallest_quick(lista, k)
            end_time = time.perf_counter()

            tempo_execucao = end_time - start_time
            tempos_execucao.append(tempo_execucao)

        media_tempo = sum(tempos_execucao) / num_repeticoes

        resultados.append({
            'Tamanho da lista': tamanho,
            'Tempo Médio (s)': media_tempo,
            'Lista Ordenada': ordem_lista
        })

    arquivo_saida = 'worst_experimentos_quick.csv'
    
    if os.path.isfile(arquivo_saida):
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(arquivo_saida, mode='a', header=False, index=False)
    else:
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(arquivo_saida, index=False)

tamanhos_listas = [500, 1000, 1500, 2000, 3000]

executar_experimentos(tamanhos_listas)
