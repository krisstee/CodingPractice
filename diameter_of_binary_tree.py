# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if(not root):
            return(0)
        if(root.left == None and root.right == None):
            return(0)
        
        self.determineEdgesCount(root, 0)
        return(self.answer - 1)
    
    def determineEdgesCount(self, root: TreeNode, count: int) -> int:
        if root:
            count_left = self.determineEdgesCount(root.left, count)
            count_right = self.determineEdgesCount(root.right, count)
            count = max(count_left, count_right) + 1
            self.answer = max(self.answer, count_left + count_right + 1)
        return(count)
        
# Intial thoughts:
# -Depth first search for each node to determine it's distance between
# another node in the tree
# -We only need to return the length, so we can have a counter that gets updated whenever
# we calculate a larger value, we don't have to cache a node's history for long
# -Keep in mind that there are instances which the node my not be included
# -The "end of the line for searching" for a node is when we "bubble up" back to a node
# that has no children
# - **** The path is left_depth + right_depth + 1

# What can I begin to build?
# - The means to reach the leaves of the node
# - With that, we can count how many "edges" we had to go through to get to the node

# Steps:
# Determine max depth of a node from its left and right sides and track them
# The answer is the max depth from the left and the max from the right. This is tracked
# separately from an overall count of depth at a level
