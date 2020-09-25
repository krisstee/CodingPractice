import collections

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Approach:
        Push the letters of s into a deque
        Run through t and popleft the deque when it's encountered
        If the deque is empty, then s is a subsequence of t

        Adding letters to deque is O(n)
        Going through t is O(n)
        Checking the length of the deque is O(n)
        """

        sdeque = collections.deque()
        for letter in s:
            sdeque.append(letter)

        t_len = len(t)
        counter = 0
        while(len(sdeque) != 0 and counter < t_len):
            nextletter = sdeque.popleft()
            if t[counter] != nextletter:
                sdeque.appendleft(nextletter)
            counter += 1

        if(len(sdeque) == 0):
            return(True)
        else:
            return(False)
