# Datastructure
import array as arr


"""
Array operation
1. creating a array
2. inserting a element
3. searching a element
4. delete a element
5. getting a value
6. setting a value

"""

# creating a element
class arrays:

    # initialization
    def __init__(self):
        self.arrays = arr.array('i',[])

    # Creting a array
    def create_arr(self,values):
        # Check user enter a value
        element = list(values)
        if not element:
            return "Please enter a element"
        # iterate list to append every value
        for i in element :
            self.arrays.append(i)
        if self.arrays:
            return f"Creating a array : {self.arrays}"
        
        print("Something a gonna wrong")

    # inserting a element
    def insert_ele(self,index,element):
        # inserting a element
        value = element
        position = index
        
        # Checking lenght of array > position
        if position > len(self.arrays):
            return "Position is not the array"
        
        self.arrays.insert(position,value)
        return f"Inserting a value : {self.arrays}"
    
    # searching operation
    def searching(self,value):
        arrs = self.arrays
        for i in range(0,len(arrs)):
            if arrs[i] == value:
                return f"Searching Index Is : {i}"
    
    # Delete opearation
    def delete_op(self,value):
        arrs = self.arrays
        if value not in arrs:
            return f"it does not exists value in arr : {value}"
        arrs.remove(value)
        return f"Successfully remove the {value} in {arrs}"

    # gettting a value
    def getting(self, index):
        arrs = self.arrays
        if index > len(arrs):
            return "Your index value does not exisiting" 
        return f"index value : {arrs[index]}"

    # Setting a value
    def setting(self,index, value):
        arrs = self.arrays
        arrs[index] = value
        return f"Modified a arr : {arrs}"


# To store the class in variable
oper = arrays()
lis = [1,2,3,4,5]
print(oper.create_arr(lis))
print(oper.insert_ele(3,10))
print(oper.searching(3))
print(oper.delete_op(1))
# another creating a list
li = [6,7,8,9,10,11,12,13,14,15]
print(oper.create_arr(li))
print(oper.getting(5))
print(oper.setting(4,4))