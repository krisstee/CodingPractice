from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create dictionary that holds compliments
        compliments = {}
        for i in range(len(nums)):
            compliments[target - nums[i]] = (nums[i], i)

        # Go through the numbers and determine the indices which add to the
        # target
        for i in range(len(nums)):
            # Determine if this number is a key in compliments
            if nums[i] in compliments:
                digit = compliments[nums[i]][0]
                location = compliments[nums[i]][1]
                if location != i:
                    return[i, location]

# Create test cases
test = Solution()
nums = [2,7,11,15]
first = test.twoSum(nums, 9)
print("input: ([2,7,11,15], 9)")
print("answer: %s\n" % first)

nums = [3,2,4]
second = test.twoSum(nums, 6)
print("input: ([3,2,4], 6)")
print("answer: %s\n" % second)

nums = [3,3]
third = test.twoSum(nums, 6)
print("input: ([3,3], 6)")
print("answer: %s\n" % third)

# Initial thoughts:
# It is not guaranteed that the list given is sorted
# There is only one valid answer
# It seems that we can't use a number twice
# -> for target = 6 we could use [3,3] but not [3]
# The answer and each given digit can be held in memory
# 2 <= len(nums) <= 10^5
# We are returning indices (something need to be able to track)

# Approach idea:
# Go through the numbers in nums
# Create a dictionary which the key is (target - number) and value is number
# Then go through the numbers again and determine if it's a key in the
# dictionary
# That way we know that a compliment that was set as a key also exists in the
# list. They key's value should be a number that exsits in the list as well.
# Check that the key's value is in nums[:key's index - 1]
# --> however, does this address when the target = 6 and list is [1,3,2,4]?

# Fix:
# We may have to look up the key, and then determine if it's compliment was
# something we already came across (exists within nums[:key's index - 1])

# Creating a dictionary is O(n)
# Looking up a key in a dict is O(1)
# Going through nums again is O(n) at most
# Determining if a number is within nums[:x] is O(n) at average
# --> Fix: dictionary is {key: (number, number's index)}
