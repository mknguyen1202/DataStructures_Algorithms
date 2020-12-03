class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None


    def printList(self):
        curr = self.head

        while curr:
            print(curr.value)
            curr = curr.next
        print("done printing")
    
    def add(self, value):
        curr = self.head
        if not curr:
            curr = Node(value)
            self.head = curr
            return

        while curr.next:
            # print(head.data)
            curr = curr.next
        
        curr.next = Node(value)

    def insert(self, value, pos):
        curr = self.head
        if not curr:
            add(value)
            return

        index = 0
        while index < pos - 1 and curr.next:
            curr = curr.next
            index += 1
        
        print(index, curr)
        if not curr.next:
            print("new node?")
            curr.next = Node(value)
            return

        temp_node = curr.next
        new_node = Node(value)
        new_node.next = temp_node
        curr.next = new_node



    def remove(self, value: int) -> Node:
        curr = self.head
        removedNode = None
        if not curr:
            return
        elif curr.value == value:   # if remove the top notch
            self.head = curr.next
            removedNode = curr.next
            curr.next = None    # clear pointer
            return removedNode
            

        while curr.next:
            if curr.next.value == value:
                temp = curr.next.next
                curr.next.next = None   # clear pointer
                removedNode =  curr.next
                curr.next = temp
                return removedNode
            

            curr = curr.next

        return removedNode

    def removeAll(self):
        self.head = None

    def search(self, value) -> Node:
        curr = self.head
        if not curr:
            return None

        while curr.next:
            if curr.value == value:
                return curr
            
            curr = curr.next


if __name__=='__main__':

    llist = LinkedList()
    llist.printList()

    llist.add(1)
    llist.add(2)
    llist.add(3)

    llist.printList()

    llist.insert(4, 1)
    llist.printList()

    llist.insert(9, 1)
    llist.insert(10,1)
    llist.printList()


    llist.remove(10)
    llist.remove(1)
    llist.remove(15)
    llist.printList()

    llist.insert(9, 1)
    llist.insert(10,1)
    llist.printList()

    item = llist.search(15)
    print(item.value)