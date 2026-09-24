class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            # length of each word + delimiter '#'
            res += str(len(word))+'#'+word

        return res

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0 # start from beginning

        while i < len(s): # i, j two pointers
            j = i 
            while s[j] != '#':
                j += 1 # get the index of '#'
            
            length = int(s[i:j]) # get the integer of the length (before #)
            i = j + 1 
            j = i + length 

            origin = s[i:j]
            res.append(origin)

            i = j # update i

        return res
    


