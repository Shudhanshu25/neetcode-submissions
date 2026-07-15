class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None

        #pass1
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1
            
            else:
                count1 -= 1
                count2 -= 1

        #pass2
        count1 = 0
        count2 = 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

        res = []
        limit = len(nums) // 3

        if count1 > limit:
            res.append(candidate1)
        
        if count2 > limit:
            res.append(candidate2)
        
        return res
        