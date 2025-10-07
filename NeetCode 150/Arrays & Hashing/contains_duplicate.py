class Solution:
    # O(n) time
    # O(n) space        easy peasy
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
            
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4, 5, 6]))