class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        all_ana = defaultdict(list) # Solution: Hashmap

        for i, s in enumerate(strs):
            count = [0]*26 # from a to z 
            for ch in s:
                count[ord(ch) - ord('a')] += 1 # use ASCII 

            all_ana[tuple(count)].append(s) # list cannot be a dictionary key; instead use tuple (not mutable)

        return list(all_ana.values())            

