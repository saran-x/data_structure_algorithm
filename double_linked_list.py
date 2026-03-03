# Double linked list

# creating a node

class node:
    def __init__(self,data):
        self.prev = None
        self.data = data 
        self.next = None

# core concept of the double linked list
class double_linked_list:
    def __init__(self):
        self.head = None
       
    # creating double linked list
    def head_double(self,data):

        current_node = node(int(data))
        if self.head is None:
            self.head = current_node
        else:
            current_node.next = self.head
            self.head.prev = current_node
            self.head = current_node
        
        # display function
        self.display()

    # Inserting a last node
    def inserting_last(self,value):
        # creating a node
        current_node = node(int(value))

        # Checking if there is no value
        if self.head == None:
            self.head_double(int(value))
            return
        # travel the last node
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = current_node
        current_node.prev = temp
        self.display()

    # Inserting a index value
    def index_value(self,index,value):
        
        # Check if not index 
        if index < 0:
            print("indexoutofbound Error")
            return
        
        # check value if index == 0 
        if index == 0:
            self.head_double(int(value))
            return
        
        # iterate a for loop
        temp = self.head
        
        for _ in range(int(index)-1):
            temp = temp.next
        
        current_node = node(value)
        
        # if value is last index
        if temp.next == None:
            temp.next = current_node
            current_node.prev = temp 

        # if value is middle
        else:
            current_node.prev = temp
            current_node.next = temp.next
            temp.next.prev = current_node
            temp.next = current_node
        self.display()

    # deleting a function
    def delete(self,value):
        # if delete value is head
        if self.head.data == value:
            self.head.next.prev = self.head.prev
            self.head = self.head.next
            self.display()
            return
        
        # check there is no node
        if self.head is None:
            print("There is no element are here !")
        temp = self.head
        
        # delete value is middle
        while temp.next != None:
            if temp.next.data == value and temp.next.next != None:
                    print(f"Delete a value : {value}")
                    temp.next = temp.next.next
                    temp.next.prev = temp
                    self.display()
                    return        
            temp = temp.next    
        
        # Deleting last value
        if temp.data == value:
            print(f"Delete a value : {value}")  
            current_node = temp # last node
            current_node.prev.next = temp.next
            self.display()
            return
        
        print(f"Value not found : {value}")
        self.display()
    def display(self):
        temp = self.head

        while temp != None:
            nodes_next = temp.next.data if temp.next else "Null" 
            nodes_prev = temp.prev.data if temp.prev else "Null"
            print(f"[{nodes_prev} | {temp.data} | {nodes_next}] <--> ", end="")
            temp=temp.next

        print("null")

args = double_linked_list()
# Inserting a Head node
args.head_double(10)
args.head_double(30)
# inserting a last node
args.inserting_last(40)
args.inserting_last(50)
args.inserting_last(60)
# inserting a index,value
args.index_value(2,80)
# Deleting a value
args.delete(40)
args.delete(80)
args.delete(100)