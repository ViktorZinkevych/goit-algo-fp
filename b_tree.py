import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#333333"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
    plt.title(title)
    plt.show()


def generate_color(index, total):
    intensity = int(255 * (index + 1) / total)
    return f'#{intensity:02x}{intensity:02x}ff'


def dfs_colored(root):
    stack = [root]
    visited = set()
    order = []

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            stack.append(node.right)
            stack.append(node.left)

    for i, node in enumerate(order):
        node.color = generate_color(i, len(order))


def bfs_colored(root):
    queue = deque([root])
    visited = set()
    order = []

    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            order.append(node)
            queue.append(node.left)
            queue.append(node.right)

    for i, node in enumerate(order):
        node.color = generate_color(i, len(order))

#  Побудова дерева
root = Node("A")
root.left = Node("B")
root.left.left = Node("D")
root.left.right = Node("E")
root.right = Node("C")
root.right.left = Node("F")

#  Візуалізація DFS
dfs_colored(root)
draw_tree(root, title="DFS")

#  Скидаємо кольори
for node in [root, root.left, root.left.left, root.left.right, root.right, root.right.left]:
    node.color = "#333333"

# Візуалізація BFS
bfs_colored(root)
draw_tree(root, title="BFS")