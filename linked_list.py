# Linked list algorithm

# Creating a node 
class node:
    def __init__(self,data):
        self.data = data # This is a node data
        self.next = None # This is a next node connection

# Linked list core concept

class linked_list:

    def __init__(self):
        self.head = None # Initially head is none 

    def insert_head(self,value):

        # Creating node
        head_node = node(int(value)) # Calling  node class to creating a node "value must me integer !"

        # Head_node next assign
        head_node.next = self.head # Initially head none 

        # Next update head to new head node
        self.head = head_node

        # To display function show output
        self.display()
    
    def insert_last(self,value):
        
        # Check head is none 
        if self.head == None:
            self.insert_head(value)
            return

        # To iterate a head next node
        temp = self.head

        # Condition runs on null value
        while temp.next != None:
            temp = temp.next

        # Create a node 
        last_node = node(int(value))

        temp.next = last_node
        self.display()

    def index_value(self,index,data):
        temp = self.head
        # if index < 0 
        if index < 0 :
            print(f'Your index value not position {index}')

        # if index value is 0
        if index == 0:
            self.insert_head(int(data))
            return

        # Iterate a position                            ----> list index based index the value
        for _ in range(index - 1):                    # ----> if you want position based insert a value change the range(1, index -1) !
            temp = temp.next 
        
        # create a new insert node
        new_node = node(int(data))
        new_node.next = temp.next
        temp.next = new_node
        self.display()

    def display(self):
        # To reference memeory for next node
        temp = self.head
        
        # To iterate until next node is null
        while temp != None:
            print(f"{temp.data} --> ",end = '')

            # To moving a next node
            temp = temp.next
        
        # If next value is None
        print("Null")


    def delete_fun(self,data):
        temp = self.head
        if self.head == None:
            print("There is no value")
            return

        # check whether delete value will be head node if head node is delete
        if self.head.data == data:
            self.head = temp.next
            print(f"Delete the value : {data}")
            self.display()
            return
        # Iterating a delete value
        while temp.next is not None:
            if temp.next.data == data:
                temp.next = temp.next.next
                print(f'Delete value : {data}')

                self.display()
                return
            temp = temp.next
        
        # If not in value node
        print(f'data not found {data}')
        self.display()
        

# To linkedlist class to store a variable
args = linked_list()

# Inserting a Head node
print("Inserting a Head Node")
args.insert_head(30)
args.insert_head(20)
args.insert_head(10)

# Inserting a last node
print("Inserting a Tail Node")
args.insert_last(40)
args.insert_last(50)

# Inserting a index based
print("Index based insert a value")
args.index_value(3,100)

# Deleting a value
print("Delete the value")
args.delete_fun(10)
args.delete_fun(100)