class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # If the strings match return True. If they do not match and either of
        # the strings is empty, return False
        if(s == t):
            return(True)
        elif(s == "" and t != ""):
            return(True)
        elif(t == ""):
            return(False)

        # Determine if we have a match of strings
        return(self.matchChars(s, t, 0, 0))

    def matchChars(self, s: str, t:str, s_place: int, t_place: int) -> bool:
        # If we went through the whole s string, we have confirmed it's
        # a subsequence
        # Otherwise, if we went through the whole t string but not s, then s is
        # not subsequence
        if(s_place == len(s)):
            return(True)
        elif(t_place == len(t) and s_place < len(s)):
            return(False)
        elif(s[s_place] == t[t_place]):
            return(self.matchChars(s, t, s_place+1, t_place+1))
        elif(s[s_place] != t[t_place]):
            return(self.matchChars(s, t, s_place, t_place+1))
