from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return f'Node: {self.data}'

test1 = Node(2)
print(test1)

@dataclass
class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.nextNode
        nodes.append('None')
        return '->'.join(nodes)

    def insertAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertAtTail(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        last = self.head
        while last.nextNode:
            last = last.nextNode
        last.nextNode = newNode


    def insert(self, prevNode, data):
        if not prevNode:
            print("Previous node is not given.")
            return
        newNode = Node(data)
        newNode.nextNode = prevNode.nextNode
        prevNode.nextNode = newNode

    def delete(self, prevNode, data):
        if not prevNode:
            print("Previous node is not given.")
            return
        
llist = LinkedList()
print(llist)

firstNode = Node('A')
llist.head = firstNode
secondNode = Node('B')
thirdNode = Node('C')

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

print(llist)


llist.insertAtTail("x")
llist.insert(llist.head, "y")
llist.insertAtHead("z")
print(llist)