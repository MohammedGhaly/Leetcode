class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        i, j, r = 0, 0, 0
        res = (m+n)*[0]
        while i < m and j < n:
            if nums2[j] < nums1[i]:
                res[r] = nums2[j]
                j += 1
            else:
                res[r] = nums1[i]
                i += 1
            r += 1
        if (i == m):
            res = res[0:i+j] + nums2[j:]
        else:
            res = res[0:i+j] + nums1[i:]
        for t in range(n+m):
            nums1[t] = res[t]


nums1 = [1, 2, 5, 0, 0, 0]
nums2 = [2, 3, 8]
sol = Solution()
sol.merge(nums1, 3, nums2, len(nums2))
print(nums1)
