import sys
import os
import argparse
import time
# ... outros imports de bibliotecas padrão ...

# CORREÇÃO CRÍTICA DO CAMINHO:
# Adiciona o diretório pai (paper_project/) ao caminho de busca do Python.
# Isso permite que 'main.py' dentro de 'tests/' encontre 'graph/'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)

# Agora os imports abaixo funcionarão corretamente:
from graph.graph import Graph
from graph.dijkstra import run_dijkstra
from graph.bellmanford import run_bellman_ford


def run_tests(json_file):
    print(f"--- Carregando Grafo: {json_file} ---")

    g = Graph()
    try:
        # AQUI: O arquivo é carregado diretamente
        g.load_from_json(json_file)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{json_file}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler o JSON: {e}")
        return

    if not g.nodes:
        print("Erro: O grafo está vazio.")
        return

    # Define o nó de origem (pega o primeiro que aparecer no set, ou fixa um se preferir)
    start_node = sorted(list(g.nodes))[0]
    print(f"Origem definida como: {start_node}")
    print(f"Total de Vértices: {len(g.nodes)}")

    # ---------------------------------------------------------
    # TESTE DIJKSTRA
    # ---------------------------------------------------------
    print("\n[1] Executando Dijkstra...")
    start_time = time.perf_counter()
    try:
        # A função agora tem um contador interno que estoura se houver loop
        dist_d, _ = run_dijkstra(g, start_node)
        duration = time.perf_counter() - start_time
        print(f"✅ Sucesso. Tempo: {duration:.6f}s")
        # print(f"   Distâncias: {dist_d}") # Descomente se quiser ver os valores
    except ValueError as e:
        print(f"❌ FALHA CONTROLADA: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado no Dijkstra: {e}")

    # ---------------------------------------------------------
    # TESTE BELLMAN-FORD
    # ---------------------------------------------------------
    print("\n[2] Executando Bellman-Ford...")
    start_time = time.perf_counter()
    try:
        dist_b, _ = run_bellman_ford(g, start_node)
        duration = time.perf_counter() - start_time
        print(f"✅ Sucesso. Tempo: {duration:.6f}s")
    except ValueError as e:
        print(f"⚠️ Detecção de Ciclo Negativo: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado no Bellman-Ford: {e}")


if __name__ == "__main__":
    # Configuração para receber argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Executa algoritmos de caminho mínimo em um grafo JSON.")
    parser.add_argument("arquivo", type=str, help="Caminho para o arquivo JSON de entrada")

    args = parser.parse_args()

    run_tests(args.arquivo)