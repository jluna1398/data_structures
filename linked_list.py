class Node:
    # constructor
    def __init__(self):
        self.head = None
        self.data = None
        self.next = None

    # setting data field to the node
    def setData(self, data):
        self.data = data

    # getting next field to the node

    def getData(self):
        return self.data

    # setting next field to the node
    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def hasNextNode(self):
        return self.next is not None

    # counting list element
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.getNext()
        return length

    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.listLength() == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        currentNode = self.head
        while currentNode.getNext() is not None:
            currentNode = currentNode.getNext()
        currentNode.setNext(newNode)
        self.lenght +=1

    def insertatPosition(self, position, data):
        # check position and length
        if position > self.lenght or position < 0:
            return None
        else:
            if position == 0:
                self.insertAtBeginning(data)
            else:
                # create a new instance of the node class
                newNode = Node()
                newNode.setData(data)
                count = 0
                currentNode = self.head
                while count< position-1:
                    count += 1
                    current = currentNode.getNext()
                newNode.setNext(currentNode.getNext())
                currentNode.setNext(newNode)
                self.length += 1









def linkList():
    ll = Node()
    return ll.head

linkList()
