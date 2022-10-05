"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].

"""
import unittest
import random

def solution(A):
    A.sort()
    
    missingElemFound = False
    i = 0
    j = 1
    
    
    while missingElemFound == False:
        if A == []:
            return 1
            
        if (A[j] - A[i]) == 1:
            i = i + 1
            j = j + 1
        else:
            missingElemFound == True
            return (A[i] + 1)

solution([2, 3, 1, 5])


ARRAY_RANGE = (-1000, 1000)
INT_RANGE = (0, 100000)


class testPermMissingElem(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(solution([1, 2, 3, 5, 6, 7, 8, 9, 10]), 4)

    def test_empty(self):
        self.assertEqual(solution([]), 1)

    def test_random(self):
        N = random.randint(*INT_RANGE)
        A = [random.randint(*ARRAY_RANGE) for _ in range(0, N)]
        print(N, A)
        print(solution(A))


if __name__ == "__main__":
    unittest.main()