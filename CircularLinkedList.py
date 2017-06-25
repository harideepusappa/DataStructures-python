class Link:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = Link(None, None) 
        self.head.next = self.head  

    def add(self, data):             
        self.head.next = Link(data, self.head.next)

    def __contains__(self, data):    
        current = self.head.next
        while current != self.head:
            if current.data == data: 
                return True
        return False