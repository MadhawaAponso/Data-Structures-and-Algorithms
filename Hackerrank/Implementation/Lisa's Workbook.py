# My Code ########################################################################################################################################
def workbook1(n, k, arr):
    # Write your code here
    count=0
    a=0
    h = []
    for x in arr:
        l = []
        a +=1
        for y in range(x):
            if(len(l)>=k):
                h.append(l)
                l = []
            l.append(y+1)
        h.append(l)
    number = 0
    for x in h:
        number+=1
        if(number in x):
            count+=1
    return count 

# More OPtimized Code###########################################################################################################################

def workbook2(n, k, arr):
    special_problems = 0
    current_page = 0
    
    for problems_in_chapter in arr:
        current_page += 1
        for problem_number in range(1, problems_in_chapter + 1):
            if problem_number == current_page:
                special_problems += 1
            if problem_number % k == 0 or problem_number == problems_in_chapter:
                current_page += 1
    
    return special_problems


n = 5
k = 3
arr = [4, 2, 6, 1, 10]
print(workbook1(n, k, arr))
