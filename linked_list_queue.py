# creating a node
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

# core concept of the linked list queue
class linked_list_queue:
    def __init__(self):
        self.first = None
        self.rear = -1

    # enqueue that means inserting a node
    def enqueue(self,data):

        # creating a node
        new_node = node(int(data))

        # whether check if empty list data
        if self.first == None:
            new_node.next = self.first
            self.first = new_node
            self.display()
            self.rear = 0
            
            return
        else: 
            # if already node is there to inserting a last node
            temp = self.first

            while temp.next != None:
                temp = temp.next
            
            # inserting a last node
            temp.next = new_node

            # rear update
            self.rear += 1
            
            # display the node
            self.display()

    # dequeueu
    def dequeue(self):
        
        # whether first node is none it is a empty queue
        if self.first == None:
            return 'Empty queue'
       
        print(f"Pop the first node : {self.first.data}")
        temp = self.first.next
        self.first = temp
        self.rear -= 1
        self.display()
        

    # display the linked function
    def display(self):
        temp = self.first
        while temp != None:
            print(f"{temp.data} --> ",end='')
            temp = temp.next

        print('Null')

# To implement of the class
args = linked_list_queue()

# to inserting a node
args.enqueue(10)
args.enqueue(20)
args.enqueue(30)
args.enqueue(40)
args.enqueue(50)

# pop the first node
args.dequeue()
args.dequeue()