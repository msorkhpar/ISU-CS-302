import matplotlib.pyplot as plt
import networkx as nx

from utils.loader import load_base_configs


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(tree, n):
    if tree is None:
        tree = Node(n)
        return tree
    if tree.data == n:
        return tree
    if tree.data < n:
        tree.right = insert_node(tree.right, n)
    else:
        tree.left = insert_node(tree.left, n)
    return tree

def add_nodes_edges(tree, graph, parent_name, pos, x=0, y=0, layer=1):
    if tree is not None:
        graph.add_node(tree.data)
        pos[tree.data] = (x, y)
        if parent_name is not None:
            graph.add_edge(parent_name, tree.data)
        if tree.left:
            l = x - 1 / 2 ** layer
            add_nodes_edges(tree.left, graph, tree.data, pos, x=l, y=y-1, layer=layer+1)
        if tree.right:
            r = x + 1 / 2 ** layer
            add_nodes_edges(tree.right, graph, tree.data, pos, x=r, y=y-1, layer=layer+1)

def draw_tree(tree_root):
    graph = nx.Graph()
    pos = {}
    add_nodes_edges(tree_root, graph, None, pos)
    nx.draw(graph, pos=pos, with_labels=True, arrows=False)
    plt.show()


if __name__ == "__main__":
    # Assuming you have a function load_base_configs() and it returns a dictionary-like object for 'env'
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    tree = None
    for a in arr:
        tree = insert_node(tree, a)
    draw_tree(tree)
