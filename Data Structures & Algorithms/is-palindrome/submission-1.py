class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Two Pointers: O(n)

        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum(): # only alphanumeric 
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower(): # case-sensitive
                return False 

            left += 1
            right -= 1 

        return True
        