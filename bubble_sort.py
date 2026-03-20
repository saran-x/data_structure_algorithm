# bubble sort 

def bubble_sort(arr):
    
    # algorithm concept
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):

            # checking condition current node is greaterthan next node to swap
            
            if arr[j] > arr[j+1]:
                
                # swap the value
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
        
    return arr

def testing():
    arr1 = [9,2,4,0,10,3,10,40,50]
    print(bubble_sort(arr1))

    arr2 = [10, 50, 20, 40, 30]
    print(bubble_sort(arr2))

    arr3 = [100, 25, 75, 50, 1] 
    print(bubble_sort(arr3))
    
    arr4 = [31, 44, 17, 78, 69]
    print(bubble_sort(arr4))

    arr5 = [5, 2, 8, 1, 9]
    print(bubble_sort(arr5))
testing()