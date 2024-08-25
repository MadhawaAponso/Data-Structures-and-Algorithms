import time

l = [12, 45, 3, 46, 23, 1, 56, 56, 90, 16]

def selectionsort(l):
    n = len(l)
    for x in range(n - 1):
        min_index = x
        for y in range(x+1, n):
            if l[y] < l[min_index]:
                min_index = y 
        l[x], l[min_index] = l[min_index], l[x]
        
    return l


start_time = time.time()

sorted_list = selectionsort(l)

end_time = time.time()
time_taken = (end_time - start_time)*1000000

print(f"Sorted List: {sorted_list}")
print(f"Time taken to sort the list: {time_taken} seconds")
