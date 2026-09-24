class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ## Using Hash Table (Better Optimal)

        if len(s) != len(t):
            return False 

        count = [0] * 26 # a to z 
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(t[i]) - ord('a')] -= 1 # check if all count values are 0 (same)

        for num in count:
            if num != 0: # if there is any non-zero (different character, frequency)
                return False 
        
        return True # all is 0 and frequency same

        