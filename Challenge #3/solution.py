from itertools import permutations

# L is a list
#   will have between 1 to 9 elements, each element is a digit between 1 and 9 
# find the largest multiple of 3 using the numbers in the list
# if there is no multiple of 3, return 0
def solution(L):
    # code here
    # for each element in the list L
    m = 0
    for i in range(len(L)+1):
        for sublist in permutations(L, i):
            print(sublist)
            perm = ""
            for j in sublist:
                perm += str(j)
            if perm != '':
                if int(perm) % 3 == 0 and int(perm) > m:
                    m = int(perm)
    return m



print(solution([3, 1, 4, 1]))
print(solution([3, 1, 4, 1, 5, 9]))