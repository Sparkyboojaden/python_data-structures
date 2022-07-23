class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = new_node

    def length(self):
        length = 0
        current = self.head
        while(current.next != None):
            length += 1
            current = current.next
        return length

    def display(self):
        values = []
        current = self.head
        while(current.next != None):
            current = current.next
            values.append(current.data)
        print(values)

    def get(self, loc):
        if(loc > self.length()):
            return "invalid location for a get"
        current = self.head
        while(loc != 0):
            current = current.next
            loc -= 1
        print(current.data)

    def delete(self, loc):
        if(loc > self.length()):
            return "invalid location for a deletion"
        list_index = 0
        current = self.head
        while(True): 
            last_node = current
            current = current.next
            if(list_index == loc):
                last_node.next = current.next
                return
            list_index += 1


ll = linked_list()
ll.append(5)
ll.append(4)
ll.append(3)
ll.append(2)
ll.append(6)
ll.display()
ll.delete(0) #index location
ll.display()
        
        

