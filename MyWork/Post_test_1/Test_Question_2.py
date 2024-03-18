class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def __repr__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        """
        Adds new node to the end of the linked list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        if self.head.nextNode is None:
            current = self.head
        else:
            current = self.tail
        current.nextNode = new_node
        self.tail = new_node

    def delete(self, data):
        """
        Deletes the selected node from the linked list
        """
        if self.head is not None:
            node = Node(data)
            if node.data == self.head.data:
                self.head = self.head.nextNode


    def display(self):
        """
        Displays the linked list

        *Note: Wasn't able to get to work unless chosen node to delete is the head of the linked list
        """
        if self.head is not None:
            node = self.head
            while node is not None:
                print(node, '-> ', end='')
                node = node.nextNode

    def length(self):
        """
        Returns the length of the linked list
        """
        count = 0
        if self.head is not None:
            node = self.head
            while node is not None:
                count += 1
                node = node.nextNode
        return count


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(5)
linked_list.insert(7)

linked_list.display()
print("\nLength of the linked list:", linked_list.length())
