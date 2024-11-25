import time
import random
import pandas as pd
import os

def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lista[k] = left[i]
                i += 1
            else:
                lista[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lista[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lista[k] = right[j]
            j += 1
            k += 1

def kth_smallest_merge(lista, k):
    merge_sort(lista)
    return lista[k - 1]

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
            lista = random.sample(range(1, 10000), tamanho)
            k = tamanho // 2

            ordem_lista = verificar_ordem(lista)

            start_time = time.perf_counter()
            kth_smallest_merge(lista, k)
            end_time = time.perf_counter()

            tempo_execucao = end_time - start_time
            tempos_execucao.append(tempo_execucao)

        media_tempo = sum(tempos_execucao) / num_repeticoes

        resultados.append({
            'Tamanho da lista': tamanho,
            'Tempo Médio (s)': media_tempo,
            'Lista Ordenada': ordem_lista
        })

    arquivo_saida = 'resultados_experimentos_merge.csv'
    
    if os.path.isfile(arquivo_saida):
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(arquivo_saida, mode='a', header=False, index=False)
    else:
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(arquivo_saida, index=False)

tamanhos_listas = [500, 1000, 1500, 2000, 3000]

executar_experimentos(tamanhos_listas)
