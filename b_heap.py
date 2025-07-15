import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def heap_to_tree(heap):
    tree = nx.DiGraph()
    pos = {}
    nodes = []

    for i, val in enumerate(heap):
        node = Node(val)
        nodes.append(node)
        tree.add_node(node.id, color=node.color, label=node.val)

    
    for i in range(len(heap)):
        layer = i.bit_length()
        x = (i - (2**layer - 1)) / 2**layer
        y = -layer
        pos[nodes[i].id] = (x, y)

        left_i = 2 * i + 1
        right_i = 2 * i + 2

        if left_i < len(heap):
            tree.add_edge(nodes[i].id, nodes[left_i].id)
        if right_i < len(heap):
            tree.add_edge(nodes[i].id, nodes[right_i].id)

    return tree, pos


def draw_heap(heap):
    tree, pos = heap_to_tree(heap)

    colors = [data["color"] for _, data in tree.nodes(data=True)]
    labels = {node_id: data["label"] for node_id, data in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, node_size=2000, node_color=colors, arrows=False)
    plt.title("Бінарна купа у вигляді дерева")
    plt.show()


heap = [3, 5, 9, 10, 12, 13, 15]
draw_heap(heap)