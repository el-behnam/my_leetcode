class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if int(log10(i)) % 2:
                count = count + 1
        return count