"""
Binary Trees
        Root Node
        [15]
        /  \
    [10]    [ ]
  /     \
[ ]     [ ]

Node
left
right
data
"""
from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


@dataclass
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._addNode(data, self.root)

    def _addNode(self, data, node):
        if data < node.data:
            if node.left:
                self._addNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self._addNode(data, node.right)
            else:
                node.right = Node(data)

    def printTree(self):
        if self.root:
            self._viewTree(self.root)

    def _viewTree(self, node):
        if node:
            self._viewTree(node.left)
            print(node.data, end="->")
            self._viewTree(node.right)


tree = BinaryTree()
tree.add(10)
tree.add(3)
tree.add(20)
tree.add(15)
tree.add(25)

tree.printTree()
