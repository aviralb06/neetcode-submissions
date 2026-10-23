class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = float('inf')

        for i in nums:
            if i < l:
                l = i
            else:
                continue

        
        return l