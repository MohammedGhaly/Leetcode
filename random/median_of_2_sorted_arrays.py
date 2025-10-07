class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a, b = nums1, nums2
        half = (len(a)+len(b)) // 2
        if len(b) < len(a):
            a, b = b, a  # swap to run binary search in the smallest arr
        l, r = 0, len(a) - 1

        while True:
            am = (r+l) // 2
            bm = half - am - 2

            aleft = a[am] if am >= 0 else float("-infinity")
            aright = a[am+1] if am+1 < len(a) else float("infinity")
            bleft = b[bm] if bm >= 0 else float("-infinity")
            bright = b[bm+1] if bm+1 < len(b) else float("infinity")

            if aleft <= bright and bleft <= aright:
                # partitioning is correct
                if (len(a)+len(b)) % 2:  # odd
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = am-1
            else:
                l = am+1
