class Solution:
    def hammingWeight(self, n: int) -> int:
        remainder=""
        count=0

        while n > 0:
            remainder+= str(n%2)
            n = n // 2
            
        for i in remainder:
            if i =="1":
                count+=1

        return count

        

        