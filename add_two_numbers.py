# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Account for either of the numbers is an empty node
        if(l1.val == None or l2.val == None):
            return(ListNode())

        lastNode = ListNode()
        carryover = -100

        while(l1 != None or l2 != None):
            if l1 == None:
                v1 = 0
            else:
                v1 = l1.val
            if l2 == None:
                v2 = 0
            else:
                v2 = l2.val
            #print("v1: %s" % v1)
            #print("v2: %s" % v2)
            sum = v1 + v2
            ones = sum % 10
            tens = sum // 10
            # Build the answer
            if(lastNode.val == 0 and lastNode.next == None and carryover == -100):
                lastNode.val = ones
            else:
                new_place = ListNode(val=(sum + carryover), next=lastNode)
                lastNode = new_place
            carryover = tens

            # Movet to next node
            if(l1 != None):
                l1 = l1.next
            if(l2 != None):
                l2 = l2.next

        return(lastNode)

# Create test cases
# 105 + 212 = 317
f1 = ListNode(val=1)
f2 = ListNode(val=0, next=f1)
f3 = ListNode(val=5, next=f2)

s1 = ListNode(val=2)
s2 = ListNode(val=1, next=s1)
s3 = ListNode(val=2, next=s2)

test = Solution()
ans = test.addTwoNumbers(f3, s3)

# 105 + 0 = 105
zero = ListNode()
#ans = test.addTwoNumbers(f3, zero)

while(ans != None):
    print(ans.val)
    ans = ans.next

# Initial thoughts
# Start from the head node and then build the result from there
# When it comes to numbers whose sum will be >= 10, we'll need to
# separate the one's and ten's place
# To get tens place: n // 10
# To get ones place: n % 10
# Remember number is in reverse order. But the head node of the answer should
# -- be in the correct order. We may be building the answer backwards
# We might add 1 -> 0 -> 8 and 9 -> 2 -> 4 -> 5
# We might add 0 and 1 -> 0 -> 8 (in which case the answer is printing the
# -- linked list backwards)

# Steps to take:
# Create "lastNode" which is standard ListNode
# Create a variable that will hold the tens place and set it to something like
# -- -100
# Go through each element in the linked lists:
# -- If one element is None but another is not, add 0 to the valid digit
# -- Add the digits and build the answer in the following way:
# --> If the last node's .val is 0, its .next = None and the tens place holder is -100
# ----> set the last node's .val to the digit in the ones place of the sum
# ---- we just calculated. Hold the tens place of that digit
# --> Otherwise, create a new node which the .val is the ones place of the sum
# -- just calculated. Set its .next value to lastNode. Set lastNode to the
# -- newly created one.
# -- Continue through the linked lists. Adding the held tens place (even if it's 0)
