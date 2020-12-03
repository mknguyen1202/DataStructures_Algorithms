class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    
    def printList(self):
        curr = self.head

        while curr:
            print(curr.value)
            curr = curr.next
        print("done printing")


    def add(self, value):
        pass


    def insert(self, value, pos):
        pass


    def remove(self, value):
        pass

    def removeAll(self, value):
        self.head = None
        self.tail = None

    def search(self, value):
        pass


    def __str__(self):
        lst = []
        curr = self.head

        while curr:
            lst.append(curr.value)
            curr = curr.next
        print("done printing")

        return str(lst)

    