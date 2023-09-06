import matplotlib.pyplot as plt
import networkx as nx

from utils.loader import load_base_configs

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def build_tree(arr):
    n = len(arr)

    tree = []
    for i in range(n):
        tree.append(Node(arr[i]))

    for i in range(n // 2):
        tree[i].left = tree[2 * i + 1]
        if 2 * i + 2 < n:
            tree[i].right = tree[2 * i + 2]
    return tree


def add_nodes_edges(tree, graph, node, pos=None, level=0,
                    width=2., vert_gap=0.4, xcenter=0.5):
    if pos is None:
        pos = {node.data: (xcenter, 1 - level * vert_gap)}
    else:
        pos[node.data] = (xcenter, 1 - level * vert_gap)
    neighbors = []
    if node.left:
        neighbors.append(node.left.data)
        pos = add_nodes_edges(tree, graph, node.left, pos,
                              level + 1, width / 2, vert_gap,
                              xcenter - width / 2)
    if node.right:
        neighbors.append(node.right.data)
        pos = add_nodes_edges(tree, graph, node.right, pos,
                              level + 1, width / 2, vert_gap,
                              xcenter + width / 2)
    graph.add_edges_from([(node.data, neighbor) for neighbor in neighbors])
    return pos


def plot_tree(tree_root, save_path=None):
    graph = nx.DiGraph()
    pos = add_nodes_edges(tree_root, graph, tree_root)
    labels = {node: node for node in graph.nodes()}
    nx.draw(graph, pos=pos, labels=labels, with_labels=True,
            node_size=500, node_color='skyblue')
    if save_path is None:
        plt.show()
    else:
        plt.savefig(save_path)
        plt.close()


if __name__ == "__main__":
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    tree = build_tree(arr)

    plot_tree(tree[0])
