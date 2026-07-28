class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res , maxFreq = 0 , 0
        mp = {}

        for right in range(len(s)):
            mp[s[right]] = mp.get(s[right] , 0) + 1

            maxFreq = max(maxFreq , mp[s[right]])

            while (right - left + 1) - maxFreq > k:
                mp[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res       