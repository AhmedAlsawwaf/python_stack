# selection sort
# Time Complexity =  O(n^2)
# Space Complexity = O(1) 
A = [-5,3,2,1,-3,-3,7,2,2]
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] =arr[min_index],arr[i]
    return arr

print(selection_sort(A))