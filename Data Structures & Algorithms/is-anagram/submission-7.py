class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_={}
        t_={}

        for i in s:
            if i not in s_:
                s_[i] = 1
            elif i in s_:
                s_[i] +=1

        for i in t:
            if i not in t_:
                t_[i] = 1
            elif i in t_:
                t_[i] +=1     

        if s_ ==t_:
            return True

        else:
            return False