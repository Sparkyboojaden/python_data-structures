class node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

class linked_list:
    def __init__(self):
        self.head = node()
    
    def append(self, data):
        new_node = node(data)
        current = self.head
        while(current.next != None):
            current = current.next
        current.next = new_node

    def display(self):
        display_vals = []
        current = self.head
        while(current.next != None):
            current = current.next
            display_vals.append(current.data)
        print(display_vals)

    def length(self):
        count = 0
        current = self.head
        while(current.next != None):
            count += 1
            current = current.next
        
        print(count)


ll = linked_list()
ll.append(4)
ll.append(3)
ll.append(5)
ll.append(11)

ll.display()
ll.length()
