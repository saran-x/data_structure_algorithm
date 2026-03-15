# creteing a stack

class arrays_stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    # inserting a symbols
    def insert_stack(self,symb):
        self.stack.append(symb)
        self.top += 1
        return self.stack
    
    # pop the top of the stack
    def pop(self):
        if self.top == -1:
            return f"Stack is empty"
        self.stack.pop(self.top)
        self.top -= 1
        return self.stack
    
    # peek is top of the stack node
    def peek(self):
        return self.stack[self.top]
        
        
    # check whether is empty
    def isempty(self):
        if self.top == -1:
            return True
        
        return False
            
# creating a array
class b_check:
    def operation(datas):
        
        # creating a stack
        stacks = arrays_stack()
        
        
        # iterating a all element
        for i in datas:
            # whether only open symbols are append
            if i == '(' or i == '{' or i == '[':
                stacks.insert_stack(i)

            # check whether closed symbols enter
            elif i == ')' or i == '}' or i == ']':
                
                # first check stack is empty because remove the match closed symbols
                if stacks.isempty():
                    print(False)
                    return
                
                # stored a current top of the stack symbols
                current = stacks.peek()
                
                # matching closed and open symbol will poped
                if current == '[' and i == ']' or current == '{' and i == '}' or current == '(' and i ==  ')':
                    stacks.pop()
                
        # if stack is empty return true after all operation 
        if stacks.isempty():
            print(True)
            return
        
        # if it does not match a open and closed symbol automatically return false
        else:
            print(False)
            return
                
args = b_check
args.operation('{]')  # <---- type the symbols