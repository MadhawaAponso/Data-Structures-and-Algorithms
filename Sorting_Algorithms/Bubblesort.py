l= [12,45,3,46,23,1,56,56,90,16]

#print(l[:-1])

def Bubblesort(l):
    for x in range(len(l)):
        for y in range(0,len(l)-x-1):
            if l[y] > l[y+1]:
                l[y],l[y+1]=l[y+1],l[y]
            
    return l

sorted = Bubblesort(l)
print(sorted)