class Solution:
    def isPalindrome(self, s: str) -> bool:
        a= ""
        n = s.lower()


        for i in n:
            if i.isalnum():
                a += i

        if len(a) ==1:
            return True
        if len(a) == 2 and a[0] == a[1]:
            return True
        elif len(a) == 2 and a[0] != a[1]:
            return False

        if a[::] == a[len(a)::-1]:
            return True
        return False