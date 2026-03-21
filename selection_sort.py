# selection sorting

def selection_sort(arr):

    # first pointing 0 to len index
    for i in range(len(arr)):

        # min value
        mini = arr[i]
        index_min = i
        
        for j in range(len(arr)):
            if j+1 > i:
                if j+1 < len(arr):
                    if arr[j+1] < mini:
                        # update the minium value
                        mini = arr[j+1]
                        index_min = j+1
                    
                    

        
        # swapping
        temp = arr[i]
        arr[i] = mini
        arr[index_min] = temp

    return arr

# testing
def testing():
    

    arr1 = [9,2,4,0,10,3,10,40,50]
    print(selection_sort(arr1))

    arr2 = [10, 50, 20, 40, 30]
    print(selection_sort(arr2))

    arr3 = [100, 25, 75, 50, 1] 
    print(selection_sort(arr3))
    
    arr4 = [31, 44, 17, 78, 69]
    print(selection_sort(arr4))

    arr5 = [5, 2, 8, 1, 9]
    print(selection_sort(arr5))

    

testing()
            