# circular linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circular_linke_list:
    def __init__(self):
        self.head = None

    # sample testing using inserting a head node
    def head_inser_node(self,value):
        current_nod = node(int(value))
        current_nod.next = self.head
        self.head = current_nod

        self.display()

    # insert last value
    def insert_last(self,value):
        currents = node(value)
        if self.head == None:
            self.head_inser_node(value)
            return
        temp = self.head

        while temp.next != None:
            temp = temp.next
        temp.next = currents
        self.display()

    # circular list 
    def ciruclar_list(self):
        next = None
        self.prev = None
        current = self.head

        while current!=None:
            next = current.next 
            current.next = self.prev
            self.prev = current
            current = next

        self.head = self.prev
        self.display()


    def display(self):
        temp = self.head

        while temp != None:
            print(f'{temp.data} --> ',end='')
            temp = temp.next

        print("Null") 


args = circular_linke_list()
# print Head node inserting
args.head_inser_node(10)
args.head_inser_node(20)
# inserting last node
args.insert_last(30)
args.insert_last(40)
# Cirucular list
args.ciruclar_list()