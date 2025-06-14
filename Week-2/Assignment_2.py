class Node: # Defined the Node class
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

class LinkedList: # Defined the LinkedList class
    def __init__(self):
        self.head = None

    def add(self, data): # Defined the add method
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self): # Defined the print_list method
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete(self, index):  # Defined the delete method and used exception handling to handle errors and edge cases
        if self.head is None:
            raise ValueError("List is empty")

        if index < 1:
            raise ValueError("Index out of range")

        current = self.head
        if index == 1:
            self.head = current.next
            return

        for i in range(1, index - 1):
            if current.next is None:
                raise ValueError("Index out of range")
            current = current.next

        if current.next is None:
            raise ValueError("Index out of range")

        current.next = current.next.next    

List = LinkedList()
List.add(10)
List.add(20)
List.add(30)
List.add(40)
List.print_list()
List.delete(2)
List.print_list()
List.delete(4) # Error: Index out of range
List.print_list()