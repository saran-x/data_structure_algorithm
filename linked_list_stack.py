# creating a node

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

# core concept of the stack linked list
class linked_list_stack:
    def __init__(self):
        self.top = None

    # inserting a node
    def insert_node(self,data):

        # creating a node
        new_node = node(int(data))
        new_node.next = self.top
        self.top = new_node
        self.display()
    
    # pop the top node
    def pop(self):
        if self.top == None:
            print("There is data in stack")
            return
        temp = self.top.next
        print(f"Delete the top data : {self.top.data}")
        self.top = temp
        self.display()

    # view the top the data
    def peek(self):
        print(f"Top the stack value : {self.top.data}")

    # check whether stack is empty
    def isempty(self):
        if self.top is None:
            print(f"Stack is empty")
            return
        self.peek()

    # display function
    def display(self):

        temp = self.top

        while temp!= None:

            print(f'{temp.data} --> ',end = "")
            temp = temp.next
        print("Null")

args = linked_list_stack()
# inserting a node
args.insert_node(10)
args.insert_node(20)
args.insert_node(30)
args.insert_node(40)
args.insert_node(50)
args.insert_node(60)

# pop the top of the value
args.pop()

# view the top the stack
args.peek()

# check whether stack empty
args.isempty()