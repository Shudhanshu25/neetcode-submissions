class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix, count = 0 , 0
        prefixMap = {0 : 1}     # for situation like nums = [3] and k = 3

        for num in nums:
            prefix += num

            needed = prefix - k

            if needed in prefixMap:
                count += prefixMap[needed]

            prefixMap[prefix] = prefixMap.get(prefix, 0) + 1
        return count