def run_bellman_ford(graph, start_node):
    # Inicializa distâncias com infinito
    distances = {node: float('inf') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start_node] = 0

    vertices_count = graph.get_vertices_count()

    # Executa V - 1 iterações relaxando todas as arestas
    # Usamos graph.edges aqui para facilitar a iteração linear sobre arestas
    for _ in range(vertices_count - 1):
        changes = False
        for u, v, weight in graph.edges:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                previous_nodes[v] = u
                changes = True
        # Pequena otimização: se nada mudou em uma rodada, podemos parar cedo
        if not changes:
            break

    # Verifica a existência de ciclos negativos
    # Tenta relaxar mais uma vez
    for u, v, weight in graph.edges:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            raise ValueError("Ciclo negativo detectado! O algoritmo não pode convergir.")

    return distances, previous_nodes