# - Each list l will contain at least 1 element but never more than 100.
# - Each element of l will be between 1 and 100.
# - t will be a positive integer, not exceeding 250.
# - The first element of the list l has index 0. 
# - For the list returned by solution(l, t), the start index must be equal or smaller than the end index. 

# l is a list 
# t is an integer
# we want to see if there are elements in l that sum up to t which are contiguous (one after the other)
def solution(l, t):
    # Your code here
    # if len(l) == 0 or len(l) >= 100:
    #     return [-1, -1]
    # if t > 250:
    #     return [-1, -1]
    for i,j in enumerate(l):
        # print(f"The values of i and j are: {i}, {j}")
        total = 0
        sublist = []
        for k in range(i, len(l)):
            # if (l[k] > 100 or l[k] < 1):
            #     return [-1,-1]
            total += l[k]
            # print("The current total is: " + str(total))
            sublist.append(k)
            if (total == t):
                sol = []
                sol.append(sublist[0])
                sol.append(sublist[-1])
                return sol
    return [-1,-1]

print(solution([1, 2, 3, 4], 15))
print(solution([4, 3, 10, 2, 8], 12))
print(solution([10,20,30,40,50,3,7,1,4,7], 60))
print(solution([10,20,30,40,50,3,7,1,4,7], 10))
print(solution([10,20,30,40,50,3,7,1,4,7], 8))
print(solution([10,20,30,40,50,3,7,1,4,7], 160))
print(solution([250,0,0], 250))
print(solution([1,2,3,4], 15))
print(solution([4, 3, 10, 2, 8], 12))
print(solution([4, 3, 5, 7, 8], 12))
print(solution([260], 260))

    
