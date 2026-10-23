class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output =[]
        nums.sort()

        for n, num in enumerate(nums):
            if num == nums[n-1] and n > 0:
                continue

            left = n+1
            right = len(nums) -1

            while left< right:
                val = nums[left] + nums[right]+ num
                if  val > 0:
                    right -=1

                elif val < 0:
                    left +=1

                else:
                    output.append([nums[left],num,nums[right]])
                    left +=1
                    while left<right and nums[left] == nums[left -1]:
                        left +=1

        return output
            


        