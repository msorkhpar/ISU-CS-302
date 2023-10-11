import inspect
import os
import sys
from typing import List


def load_graph_from_file(edge_list_file: str) -> List[List[int]]:
    try:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        caller_file = os.path.dirname(os.path.abspath(module.__file__))

        edge_list_path = os.path.join(caller_file, edge_list_file)
        with open(edge_list_path, "r") as fp:
            while True:
                line = fp.readline()
                if line.startswith("#"):
                    continue
                else:
                    break

            n, m = map(int, line.split())

            adjacency_matrix = [[sys.maxsize if i != j else 0 for i in range(n)] for j in range(n)]

            for _ in range(m):
                a, b, weight = map(int, fp.readline().split())
                adjacency_matrix[a][b] = weight
                #adjacency_matrix[b][a] = weight
    except FileNotFoundError:
        print("No file found.")
        sys.exit(1)

    return adjacency_matrix
