class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:  #slicing string from 1st index
            while not s.startswith(prefix):
                prefix = prefix[:-1]    #slicing from the last character of the string
                if not prefix:
                    return ""
        return prefix