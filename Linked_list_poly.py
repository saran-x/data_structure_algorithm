# polynomial concept of linked list

# creating a node

class Node:
    def __init__(self,coff,expo):
        self.coff = coff
        self.expo = expo
        self.next = None

# linked list creation

class linked_list:
    def __init__(self):
        self.head = None

    # Insert last linked list

    def insert_last(self,coff,expo):

        # node creation
        new_node = Node(int(coff),int(expo))
        
        # if head is none
        if self.head == None:

            new_node.next = self.head
            self.head = new_node
            self.display()
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next

        temp.next = new_node
        self.display()

    # Display the node
    def display(self):

        # whether there is no node
        if self.head == None:
            print("There is no node is there")
            return

        temp = self.head
        while temp != None:
            print(f"| {temp.coff} | X^{temp.expo} | --> ",end = "")
            temp = temp.next

        print("Null")


# class polynomial function adding function
class poly_add:
    
    # adding concept of the 
    def poly_add_fun(self,p1,p2):
        p = linked_list()
        while p1 != None and p2 != None:
            if p1.expo == p2.expo:
                sum_coeff = p1.coff + p2.coff
                if sum_coeff != 0:
                    p.insert_last( sum_coeff , p1.expo)
                p1 = p1.next
                p2 = p2.next
            elif p1.expo > p2.expo:
                p.insert_last(p1.coff,p1.expo)
                p1 = p1.next
            elif p2.expo > p1.expo :
                p.insert_last(p2.coff,p2.expo)
                p2 = p2.next
        while p1 != None:
            p.insert_last(p1.coff,p1.expo)
            p1 = p1.next
        while p2 != None:
            p.insert_last(p2.coff,p2.expo)
            p2 = p2.next
            
        print("\n" + "="*50)
        print("RESULT OF POLYNOMIAL ADDITION:")
        p.display()
        return p


# p1 polynomial linked list
p1 = linked_list()
p1.insert_last(3,2)
p1.insert_last(4,2)
p1.insert_last(1,0)

# p2 polynomial linked list
p2 = linked_list()
p2.insert_last(4,2)
p2.insert_last(2,2)
p2.insert_last(2,0)

# poly add
p_add = poly_add()
p_add.poly_add_fun(p1.head,p2.head)