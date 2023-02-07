class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        cons = count
        reset = False
        for i in nums:
            if i == 1:
                count = count + 1 
            else:
                cons = max(cons, count)
                count = 0
        cons = max(cons, count)
        return cons