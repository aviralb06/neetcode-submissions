class Solution:
    def isPalindrome(self, s: str) -> bool:
        a= ""
        n = s.lower()


        for i in n:
            if i.isalnum():
                a += i


        if a[::] == a[len(a)::-1]:
            return True
        return False