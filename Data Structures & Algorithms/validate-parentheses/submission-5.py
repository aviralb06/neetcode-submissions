class Solution:
    def isValid(self, s: str) -> bool:
        l ={")":"(","}":"{","]":"["}
        count = 0
        stack = []

        if s[0] in "})]":
            return False

        for i in s:
            if i in "{([":
                stack.append(i)
                count += 1
            
            elif l[i] in stack and len(stack) > 0 and l[i] == stack[-1]:
                stack.pop()
                count -= 1

            else:
                return False
        return (count == 0 and stack == [])
