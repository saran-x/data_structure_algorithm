# creating a linked list


class circular_linked_list:

    class nod_creation:
        def __init__(self,data):
            self.data = data
            self.next = None

    def __init__(self):
        self.tail = None
    
    # inserted beginning
    def insert_beginning(self,data):
        # creating a new node
        new_node = self.nod_creation(int(data))

        # check whether there is no node
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
            print(f"new node inserted : {data}")

        else:
            new_node.next = self.tail.next
            self.tail.next = new_node     

            print(f"Inserted beginning : {data}")

        self.display()

    # inserted at last
    def inserted_last(self,data):
        # creating a new node
        new_node = self.nod_creation(int(data))
        # check whether there is no node is here
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node
            print(f"Inserted last node : {data}")
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
            print(f"Inserted last node : {data}")
        
        self.display()

    # Delete at beginning
    def delete_beginning(self):
        # whether there is no node is here
        if self.tail is None:
            print(f"Empty ciruclar list")
            return

        # Check whether only one node is here
        if self.tail == self.tail.next:
            self.tail = None
            print('Empty circular linked list')
            return        
        
        else:
            print(f"Delete a first node : {self.tail.next.data}")
            self.tail.next = self.tail.next.next
        
        self.display()

    # Delete at last
    def delete_last(self):
        temp = self.tail
        # whether there is no node is here
        if self.tail is None:
            print(f"Empty ciruclar list")
            return

        # Check whether only one node is here
        if self.tail == self.tail.next:
            self.tail = None
            print('Empty circular linked list')
            return     
        
        else:
            while True:
                temp = temp.next

                if temp.next == self.tail:
                    temp.next = temp.next.next
                    self.tail = temp
                    print(f"Delete last node : {self.tail.data}")
                    break
        self.display()    

    def display(self):

        temp = self.tail

        if self.tail is None:
            print(f"Empty ciruclar list")
            return


        while True:
            print(f"{temp.data} --> ",end= "")
            temp = temp.next

            if temp == self.tail:
                break
        
        print("start with beging")

args = circular_linked_list()

# Insert beginning
args.insert_beginning(0)
args.insert_beginning(1)
args.insert_beginning(2)
args.insert_beginning(3)

# Inserted last
args.inserted_last(4)
args.inserted_last(5)
args.inserted_last(6)

# Delete at first node
args.delete_beginning()
args.delete_beginning()
args.delete_beginning()

# Delete at last node
args.delete_last()
args.delete_last()