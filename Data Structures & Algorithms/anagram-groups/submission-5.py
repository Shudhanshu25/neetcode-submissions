class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}
        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - 97] += 1

            key = tuple(count)

            if key not in mpp:
                mpp[key] = []
            mpp[key].append(s)

        return list(mpp.values())
        