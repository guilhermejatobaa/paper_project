import json
from collections import defaultdict


class Graph:
    def __init__(self):
        # Hash map: chave é o nó origem, valor é lista de tuplas (destino, peso)
        self.adj_list = defaultdict(list)
        # Mantemos um set de todos os nós para saber o V (número de vértices)
        self.nodes = set()
        self.edges = []  # Lista plana de arestas para facilitar Bellman-Ford

    def load_from_json(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)

        self.adj_list.clear()
        self.nodes.clear()
        self.edges.clear()

        for edge in data:
            u, v, w = edge['from'], edge['to'], edge['weight']
            self.adj_list[u].append((v, w))
            self.edges.append((u, v, w))
            self.nodes.add(u)
            self.nodes.add(v)

    def get_vertices_count(self):
        return len(self.nodes)