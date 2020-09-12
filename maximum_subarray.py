"""
This solution was orginally written in a Google Doc to simulate
Google interview practice
"""

# initial thoughts
# The answer can be just one number
# The answer can be the whole array
# The answer may be a negative number

# The core question at every number is does this contribute the max sum?

# Dynamic programming solution with O(N) time and O(C) space
def findMaxSum(A: List[int]) -> int:
    # if A happens to be empty then we can return 0
    if(A == []):
        return(0)
    # A may be of just length = 1
    if(len(A) == 1):
        return(A[0])

    max_sum = A[0]
    n = len(A)
    for i in range(1, n):
        if A[i-1] > 0:
            A[i] += A[i-1]
                max_sum = max(A[i], max_sum)

    return(max_sum)


# ** This was an attempt to use binary search techniques
# A = [-2,1,-3,4,-1,2,1,-5,4]
# Part 1: [-2,1,-3,4,-1]
# Part 2: [2,1,-5,4]

# Creating a midpoint between in the original input (in this A[4] = -1)
# I can look at if the sum of all the left elements plus A[4] is > the sum of all
# the right elements plus A[4] (is  0 > 2)
