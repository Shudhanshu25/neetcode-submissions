class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0 , 0 
        maxLen = 0
        elem = set()

        for right in range(len(s)):
            while s[right] in elem:
                elem.remove(s[left])
                left += 1
            elem.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen
        