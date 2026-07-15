class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return nums

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = []
        limit = len(nums) // 3

        for num, count in freq.items():
            if count > limit:
                res.append(num)
        return res
        