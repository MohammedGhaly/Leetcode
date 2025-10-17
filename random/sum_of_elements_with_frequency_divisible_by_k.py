class Solution:
    def sumDivisibleByK(self, nums: list[int], k: int) -> int:
        sum = 0
        hashmap = {}
        
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        for n in hashmap:
            if (hashmap[n] % k) == 0:
                sum += (n * hashmap[n])
        
        return sum
    

sol = Solution()
nums =[1,2,2,3,3,3,3,4]
res = sol.sumDivisibleByK(nums, 2)
print(res)