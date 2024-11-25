import time
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

def executar_experimentos_best_case(tamanhos_listas, num_repeticoes=10):
    resultados = []

    for tamanho in tamanhos_listas:
        tempos_execucao = []

        for _ in range(num_repeticoes):
            lista = list(range(1, tamanho + 1))
            k = tamanho // 2

            start_time = time.perf_counter()
            kth_smallest_merge(lista, k)
            end_time = time.perf_counter()

            tempo_execucao = end_time - start_time
            tempos_execucao.append(tempo_execucao)

        media_tempo = sum(tempos_execucao) / num_repeticoes

        resultados.append({
            'Tamanho da lista': tamanho,
            'Tempo Médio (s)': media_tempo,
            'Lista Ordenada': 'Ordenada'
        })

    arquivo_saida = 'resultados_experimentos_best_case_merge.csv'
    
    if os.path.isfile(arquivo_saida):
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(arquivo_saida, mode='a', header=False, index=False)
    else:
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(arquivo_saida, index=False)

tamanhos_listas = [500, 1000, 1500, 2000, 3000]

executar_experimentos_best_case(tamanhos_listas)