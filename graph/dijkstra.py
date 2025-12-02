import heapq

def run_dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start_node] = 0
    pq = [(0, start_node)]

    # Adicionamos um freio de segurança (max_iterations) E a checagem lógica.
    iterations = 0
    max_iterations = len(graph.nodes) * len(graph.adj_list) * 2

    while pq:
        iterations += 1
        # Trava de Segurança contra loops infinitos (devemos mantê-la!)
        if iterations > max_iterations:
            raise ValueError("Falha: Dijkstra excedeu o limite de iterações. Provável ciclo negativo.")

        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph.adj_list[current_node]:

            # NOVO MECANISMO DE FALHA LÓGICA:
            # Se encontramos uma aresta com peso negativo E precisamos relaxá-la,
            # o algoritmo falhou em seu princípio e deve abortar.
            if weight < 0:
                raise ValueError(
                    f"Falha Lógica: Dijkstra encontrou a aresta negativa {current_node} -> {neighbor} com peso {weight}. O algoritmo não garante o caminho mínimo neste caso.")

            distance = current_dist + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes