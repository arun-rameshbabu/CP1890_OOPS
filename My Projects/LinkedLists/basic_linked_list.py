from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return f"Node: {self.data}"


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
            node = node.next_node
        nodes.append('None')
        return '->'.join(nodes)

    def insert_at_head(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next_node = self.head
            self.head = node

    def insert_at_position(self, node, position):
        data = self.head
        pos = 0
        if pos == position:
            self.insert_at_head(node)
        while pos + 1 < position:
            data = data.next_node
            pos += 1
        try:
            next_node = data.next_node
            data.next_node = node
            node.next_node = next_node
        except AttributeError:
            print('Out of Range.')

    def insert_at_tail(self, node):
        if self.head is None:
            self.head = node
        else:
            if self.head.next_node is None:
                self.head.next_node = node
            else:
                data = self.head
                while data.next_node is not None:
                    data = data.next_node
                data.next_node = node


linked_list = LinkedList()
print(linked_list)

first = Node('a')
linked_list.head = first

second = Node('b')
third = Node('c')

first.next_node = second
second.next_node = third

print(linked_list)

insert_head = Node(1)
linked_list.insert_at_head(insert_head)
print(linked_list)

insert_tail = Node(2)
linked_list.insert_at_tail(insert_tail)
print(linked_list)

insert_position = Node(3)
linked_list.insert_at_position(insert_position, 3)
print(linked_list)
