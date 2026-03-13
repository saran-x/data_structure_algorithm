import array

# creating a array 

class stack_array:
    def __init__(self):
        self.arr = array.array('i',[])
        self.top = -1

    # insert the array value
    def insert_value(self,element):
        
        value = int(element)
        self.arr.append(value)
        self.top += 1 

        print(self.overflow())

        return self.arr
    
    # pop the value
    def pop_fun(self):
        if self.top == -1:
            return f"Stack is Empty doesnot use pop function"
        self.arr.pop(self.top)
        self.top -= 1
        print(self.overflow())
        return self.arr
    
    # peek
    def peek(self):
        if self.top == -1:
            return f"Stack is Empty"
        return f"Stack Top value : {self.arr[self.top]}"
    
    # Stack empty check
    def empty_check(self):
        if self.top == -1:
            return f"Stack is Empty"
        return "Stack is not Empty"
    
    # Stack overflow
    def overflow(self):
        if self.top == 99:
            print(f"{self.pop_fun()}")

            return "Stack is the overflow automatically delete a last value"
        
        return f"Stack element current range : {self.top}"
    
args = stack_array()
# inserting a value
print(args.insert_value(10))
print(args.insert_value(11))
print(args.insert_value(12))
print(args.insert_value(13))
print(args.insert_value(14))

# pop the value
print(args.pop_fun())

# view the last value
print(args.peek())

# Check stack is empty
print(args.empty_check())

# check over flow
print(args.overflow())