def bubble_sort(A):
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(n-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True 
        if not swapped:
            break
    
arr = [9, 5, 4, 10, 8, 7, 1, 3, 2, 6]
bubble_sort(arr)
print("Array yang sudah diurutkan:")
print(arr)
  

