class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Hash Table
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Bucket Sorting 
        # Create frequency tables (i = frequency, value = a list of nums)
        all_freq = [[] for i in range(len(nums)+1)] # 0 to len(nums)

        for num, value in count.items():
            all_freq[value].append(num)

        # Top k -> (iterating from the last idx to i of all_freq)
        res = []

        for i in range(len(all_freq)-1, 0, -1):
            for n in all_freq[i]:
                res.append(n)
                if len(res) == k: # Top k 
                    return res


        

        

        
            

