class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        
        num_set = set(nums)
        maxLength = 0

        for num in num_set:
            if (num - 1) not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength
        