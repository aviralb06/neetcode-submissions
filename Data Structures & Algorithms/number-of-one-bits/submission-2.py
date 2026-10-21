class Solution:
    def hammingWeight(self, n: int) -> int:
        remainder=""
        count=0

        while n > 0:
            remainder+= str(n%2)
            if n%2 == 1:
                count +=1
            n = n // 2
 

        return count

        

        