# quick sort

def quicksort(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while i<j:
        while i <= high and arr[i] <= pivot:
            i += 1
        
        while j>= low and arr[j] > pivot:
            j -= 1
        
        if i < j:
            swap(arr,i,j)

        swap(arr,low,j)
    
    return j

def swap(arr,i,j):

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def quick_sorts(arr,low,high):

    if low < high:
        pivot_index = quicksort(arr, low, high)
        
        # Recursively sort elements before and after pivot
        quick_sorts(arr, low, pivot_index - 1)  # Left of pivot
        quick_sorts(arr, pivot_index + 1, high)
        
def  testing():
    arr = [5,3,8,4,2,7,1,10]
    quick_sorts(arr,0,len(arr)-1)
    print(arr)
    
testing()
