class Solution:
    def isPalindrome(self, s: str) -> bool:
        a= ""
        for i in s:
            if i.isalnum():
                a += i.lower()


        if a[::] == a[len(a)::-1]:
            return True
        return False