"""
APS - ANÁLISE DE ALGORITMOS DE ORDENAÇÃO
Versão simples: carrega dados → executa → mostra resultados
"""

import pandas as pd
import time
import tracemalloc
from algoritmos import sorts



# ==================== CARREGAR DADOS ====================

print("="*70)
print("ANÁLISE DE ALGORITMOS DE ORDENAÇÃO".center(70))
print("="*70)

# Caminho do CSV (AJUSTE AQUI SE NECESSÁRIO)
CSV_PATH = "projeto_ordenacao\data\Jogadores.csv"

print(f"\nCarregando: {CSV_PATH}")
dados = pd.read_csv(CSV_PATH)
pontos = dados["Pontos"].tolist()

print(f"{len(pontos)} jogadores carregados")
print(f"   Menor: {min(pontos)} | Maior: {max(pontos)} | Média: {sum(pontos)/len(pontos):.0f}")


# ==================== EXECUTAR ALGORITMOS ====================

print("\n" + "="*70)
print("EXECUTANDO ANÁLISE".center(70))
print("="*70)

algoritmos = {
    "Bubble Sort": sorts.bubble_sort,
    "Selection Sort": sorts.selection_sort,
    "Merge Sort": sorts.merge_sort,
    "Quick Sort": sorts.quick_sort
}

resultados = {}

for nome, funcao in algoritmos.items():
    print(f"\nExecutando {nome}...")
    
    # Medir memória
    tracemalloc.start()
    
    # Medir tempo
    inicio = time.time()
    resultado, comp, troc = funcao(pontos[:])
    fim = time.time()
    
    # Capturar memória
    _, mem_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    # Salvar
    resultados[nome] = {
        'tempo': fim - inicio,
        'memoria': mem_pico / (1024 * 1024),
        'comparacoes': comp,
        'trocas': troc
    }
    
    print(f"Concluído em {resultados[nome]['tempo']:.6f}s")


# ==================== MOSTRAR RESULTADOS ====================

print("\n" + "="*70)
print("RESULTADOS".center(70))
print("="*70)

print(f"\n{'Algoritmo':<18} {'Tempo (s)':<12} {'Memória (MB)':<14} {'Comparações':<15} {'Trocas'}")
print("-"*70)

for nome, dados in resultados.items():
    print(f"{nome:<18} {dados['tempo']:<12.6f} {dados['memoria']:<14.4f} "
          f"{dados['comparacoes']:<15,} {dados['trocas']:,}")

print("-"*70)


# ==================== RANKING ====================

print("\nRANKING POR VELOCIDADE:")
ranking = sorted(resultados.items(), key=lambda x: x[1]['tempo'])

for i, (nome, dados) in enumerate(ranking, 1):
    print(f"   {i}º - {nome}: {dados['tempo']:.6f}s")

print(f"\nMELHOR ALGORITMO: {ranking[0][0]}")
print(f"   ({ranking[0][1]['tempo']:.6f} segundos)")

# Speedup
print(f"\nCOMPARAÇÃO DE VELOCIDADE:")
tempo_base = resultados['Bubble Sort']['tempo']
for nome in ['Selection Sort', 'Merge Sort', 'Quick Sort']:
    velocidade = tempo_base / resultados[nome]['tempo']
    print(f"   {nome} é {velocidade:.2f}x mais rápido que Bubble Sort")

print("\n" + "="*70)
print("ANÁLISE CONCLUÍDA".center(70))
print("="*70)