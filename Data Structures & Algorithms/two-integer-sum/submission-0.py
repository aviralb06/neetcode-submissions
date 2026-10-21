class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for num, value in enumerate(nums):
            d[value]= num

        for num, value in enumerate(nums):
            diff = target - value
            if diff in d and d[diff] != num:
                return [num,d[diff]]

        
        

