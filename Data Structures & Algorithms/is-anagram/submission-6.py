class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        ## (1) Hash table using arrays
        count = [0] * 26 # a to z 
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(t[i]) - ord('a')] -= 1 # check if all count values are 0 (same)

        for num in count:
            if num != 0: # if there is any non-zero (different character, frequency)
                return False 
        
        return True # all is 0 and frequency same

        ## (2) Hash table using dictionary 
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1 
            countT[t[i]] = countT.get(t[i], 0) + 1 
        
        return countS == countT

        