from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            mpp[key].append(s)
        return list(mpp.values())
        