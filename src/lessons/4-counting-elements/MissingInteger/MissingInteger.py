"""

This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""

def solution(A):
    hashMap = A
    max = 1
    
    for i, h in enumerate(hashMap):
        if h >= max:
            max = h
        if h < 0:
            max = -1
        if h == 0:
            max = 0
            
    if max == 0:
        print(1)
        return 1
    if max < 0:
        print(1)
        return 1
    elif max == 1:
        print(max + 1)
        return max + 1
    else:
        if (max - 1) not in hashMap:
            print(max - 1)
            return max - 1
        else:
            print(max + 1)
            return max + 1
        

solution([0])