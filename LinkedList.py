class Node:
    def __init__(self):
        self.data = None
        self.next = None
    def __str__(self):
        return "Data %s: Next -> %s"%(self.data, self.next)

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.curNode = self.head
    def insertNode(self, data):
        node = Node()
        node.data = data
        node.next = None
        if self.head.data == None:
            self.head = node
            self.curNode = node
        else:
            self.curNode.next = node
            self.curNode = node
    def printList(self):
        print self.head

l = LinkedList()
l.insertNode(1)
l.insertNode(2)
l.insertNode(34)