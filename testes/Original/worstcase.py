import time
import random
import pandas as pd
import os

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

def kth_smallest_sort(lista, k):
    insertion_sort(lista)
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
            lista = list(range(1, tamanho + 1))[::-1]
            k = tamanho // 2

            ordem_lista = verificar_ordem(lista)

            start_time = time.perf_counter()
            kth_smallest_sort(lista, k)
            end_time = time.perf_counter()

            tempo_execucao = end_time - start_time
            tempos_execucao.append(tempo_execucao)

        media_tempo = sum(tempos_execucao) / num_repeticoes

        resultados.append({
            'Tamanho da lista': tamanho,
            'Tempo Médio (s)': media_tempo,
            'Lista Ordenada': ordem_lista
        })

    arquivo_saida = 'worst_experimentos.csv'
    
    if os.path.isfile(arquivo_saida):
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(arquivo_saida, mode='a', header=False, index=False)
    else:
        df_resultados = pd.DataFrame(resultados)
        df_resultados.to_csv(arquivo_saida, index=False)

tamanhos_listas = [500, 1000, 1500, 2000, 3000]

executar_experimentos(tamanhos_listas)
