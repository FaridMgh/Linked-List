

class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def init(self, node):
        node.setNext(self.head)
        self.head = node

    def insertBefore(self, data, newData):
        temp = self.head
        while temp:
            if temp.next:
                if temp.next.getData() == data:
                    node = Node(newData)
                    node.setNext(temp.next)
                    temp.next = node
                    return
            temp = temp.next

    def insertAfter(self, data, newData):
        temp = self.head
        while temp:
            if temp.getData() == data:
                node = Node(newData)
                node.setNext(temp.next)
                temp.next = node
                return
            temp = temp.next

    def delete(self, data):
        temp = self.head
        while temp:
            if temp.next.getData() == data:
                temp.setNext(temp.next.next)
                return
            temp = temp.next

    def deleteFirst(self):
        self.head = self.head.next

    def deleteLast(self):
        temp = self.head
        while temp:
            if temp.next.next is None:
                temp.next = None
                return
            temp = temp.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.getData(), end=" ")
            temp = temp.next
        print()


if __name__ == '__main__':

    linkedList = LinkedList()

    node1 = Node(1)

    linkedList.init(node1)
    linkedList.insertAfter(1, 2)
    linkedList.insertAfter(2, 3)

    print("First List: ", end="")
    linkedList.printList()

    print("Inserting 4 before 3: ", end="")
    linkedList.insertBefore(3, 4)
    linkedList.printList()

    print("Inserting 5 after 2: ", end="")
    linkedList.insertAfter(2, 5)
    linkedList.printList()

    print("Removing 5: ", end="")
    linkedList.delete(5)
    linkedList.printList()
