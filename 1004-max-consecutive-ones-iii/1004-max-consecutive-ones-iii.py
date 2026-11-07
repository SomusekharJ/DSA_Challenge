class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_length = 0
        left = 0
        count_zero = 0
        for i in range(len(nums)):

            if nums[i] == 0:
                count_zero += 1

            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            
            max_length = max(max_length, i - left + 1)
        
        return max_length
                    