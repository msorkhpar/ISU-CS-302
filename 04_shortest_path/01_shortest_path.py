import sys
from typing import List

from utils.loader import load_base_configs
from utils.graph_constructor import load_graph_from_file
from utils.visualize_adjacency_matrix import visualize_adj_matrix


def find_path(p, u):
    if u == 0:
        print(u, end=" ")
        return
    find_path(p, p[u])
    print(u, end=" ")


def shortest_path(graph: List[List[int]]):
    n_g = len(graph)

    distance_table = [sys.maxsize] * n_g
    path = [0] * n_g
    visited = [0] * n_g

    for i in range(1, n_g):
        distance_table[i] = graph[0][i]

    visited[0] = 1
    distance_table[0] = 0

    for _ in range(1, n_g):
        min_val = sys.maxsize
        smallest = None

        for j in range(1, n_g):
            if visited[j] == 0 and distance_table[j] < min_val:
                min_val = distance_table[j]
                smallest = j

        if smallest is not None:
            visited[smallest] = 1
            for j in range(1, n_g):
                if visited[j] == 0 and distance_table[j] > (distance_table[smallest] + graph[smallest][j]):
                    distance_table[j] = distance_table[smallest] + graph[smallest][j]
                    path[j] = smallest

    for i in range(1, n_g):
        if distance_table[i] == sys.maxsize:
            print(f"No path from 0 to {i}")
            continue
        print(f"Shortest path from 0 to {i} is {distance_table[i]}")
        find_path(path, i)
        print()


if __name__ == '__main__':
    env, logger = load_base_configs()
    edge_list_path = env.str('EDGE_LIST_PATH')
    adjacency_matrix = load_graph_from_file(edge_list_path)
    visualize_adj_matrix(adjacency_matrix)
    shortest_path(adjacency_matrix)
