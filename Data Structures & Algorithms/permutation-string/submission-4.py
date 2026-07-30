class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        matches = 0

        for i in range(26):
            if count1[i] == count2[i]:
                matches += 1
            
            if matches == 26:
                return True
        
        left = 0

        for right in range(len(s1) , len(s2)):
            leftChar = ord(s2[left]) - ord('a')

            if count1[leftChar] == count2[leftChar]:
                matches -= 1
            
            count2[leftChar] -= 1

            if count1[leftChar] == count2[leftChar]:
                matches += 1

            rightChar = ord(s2[right]) - ord('a')

            if count1[rightChar] == count2[rightChar]:
                matches -= 1
            
            count2[rightChar] += 1

            if count1[rightChar] == count2[rightChar]:
                matches += 1
            
            if matches == 26:
                return True
            left += 1
        return False
        