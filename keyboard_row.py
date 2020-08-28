"""
The followingis the solution for the Keyboard Row problem found in Leetcode
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        if(words == []):
            return([])
        
        TOP = set('QWERTYUIOP')
        MIDDLE = set('ASDFGHJKL')
        BOTTOM = set('ZXCVBNM')
        
        result = []
        
        for word in words:
            word_set = set(word.upper())
            if(word_set.issubset(TOP) or word_set.issubset(MIDDLE) or word_set.issubset(BOTTOM)):
                result.append(word)
                
        return(result)
