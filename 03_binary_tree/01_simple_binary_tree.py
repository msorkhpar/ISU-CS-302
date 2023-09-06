# https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
from __future__ import annotations

import math

from utils.loader import load_base_configs


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(node: Node):
    if node is None:
        return
    logger.info(node.data)
    pre_order(node.left)
    pre_order(node.right)


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


if __name__ == '__main__':
    env, logger = load_base_configs()
    arr = env.list('ARRAY', subcast=int)
    tree = build_tree(arr)

    logger.info(f"Pre-order traversal:")
    pre_order(tree[0])
