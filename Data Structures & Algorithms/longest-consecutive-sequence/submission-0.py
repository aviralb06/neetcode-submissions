class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num =set(nums)
        maxval = 0 


        for i in num:
            #check for the start
            if i -1 not in num:
                length = 1
                while (i+length) in num:
                    length +=1
                maxval = max(maxval,length)
        return maxval



        