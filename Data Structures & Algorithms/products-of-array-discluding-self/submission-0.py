class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        max_sum= 1
        flag = 0

        if 0 in nums:
            flag = 1
            new = nums.copy()
            new.remove(0)
            for i in new:
                max_sum = max_sum * i
        else:
            for i in nums:
                max_sum = max_sum * i

        for i in nums:
            if flag == 0:
                val = max_sum / i
                output.append(int(val))
            elif flag == 1 and i != 0:
                output.append(0)
            elif flag == 1 and i == 0:
                output.append(int(max_sum))

        return output

            


        