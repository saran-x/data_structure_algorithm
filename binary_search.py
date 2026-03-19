# function of the binary search

# assending binary search
def asend_binary_search(arr,target):
    count = 0
    first = 0
    last = len(arr) - 1
    # first we check target value in list
    while first <= last:
        mid = (first + last) // 2
        
        if arr[mid] == target  :
            return f'Target : {mid}'
        
        elif arr[mid] < target:
            count +=1
            first = mid + 1
        
        else:
            count +=1
            last = mid - 1

        count +=1         
    return -1    

# decending binary search
def decend_binary_search(arr,target):
    count = 0
    first = 0
    last = len(arr) - 1
    # first we check target value in list
    while first <= last:
        mid = (first + last) // 2
        
        if arr[mid] == target  :
           
            return f'Target : {mid}'
        
        elif arr[mid] < target:
            count +=1
            last = mid - 1
        
        else:
            count +=1
            first = mid + 1

        count +=1         
    return -1   



def tesing_case():
    # assending search
    arr1 = [3,5,15,20,22,25,32]
    print(asend_binary_search(arr1,25))

    # decending search
    arr2 = [10,9,8,7,6,5]
    print(decend_binary_search(arr2,6))

tesing_case()