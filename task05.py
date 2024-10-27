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

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(tree_root):
    stack = [tree_root]
    visited = set()
    depth = 0

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            color = f'#{depth * 15:02X}B0{255 - depth * 15:02X}'
            node.color = color
            depth += 1
            
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

def bfs(tree_root):
    queue = [tree_root]
    visited = set()
    depth = 0

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            color = f'#{depth * 15:02X}B0{255 - depth * 15:02X}'
            node.color = color
            depth += 1
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs(root)
draw_tree(root)

for node in [root, root.left, root.left.left, root.left.right, root.right, root.right.left]:
    node.color = "skyblue" 

bfs(root)
draw_tree(root)