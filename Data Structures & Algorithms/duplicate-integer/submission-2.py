class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countarray = []
        for elem in nums:
            if elem in countarray:
                return True
            countarray.append(elem)
        return False


         