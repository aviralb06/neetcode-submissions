class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = []
        prev = ""
        count = 0

        for i in range(len(s)):
            char = s[i]
            if char not in prev:
                count += 1
                prev += char
            else:
                l.append(count)
                # Cut everything up to and including the previous occurrence
                duplicate_idx = prev.index(char)
                prev = prev[duplicate_idx + 1 :] + char
                count = len(prev)

        # Catch the final substring length in case the string ends on unique characters
        l.append(count)

        return max(l)