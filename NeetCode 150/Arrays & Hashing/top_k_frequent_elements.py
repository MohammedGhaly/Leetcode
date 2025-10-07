class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]       # list of lists -->
                                                    # index:  how many times      value: number
                                                    
        for num in nums:                            # counting how many times each number appeared
            count[num] = 1 + count.get(num, 0)      # key: number       value: count
        
        for num, coun in count.items():             # filling freq list with lists
            freq[coun].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):      # iterate through the freq list from higher to lower
            for num in freq[i]:                     # indieces, keep moving values to res until we have
                res.append(num)                     # a total of k elements
                if len(res) >= k:
                    return res


sol = Solution()
print(sol.topKFrequent([1], 1))
