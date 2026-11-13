class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        def helper(x):
            if x < 0: return 0

            count = 0
            currsum = 0
            left = 0
            for i in range(len(nums)):
                currsum += nums[i]

                while currsum > x:
                    currsum -= nums[left]
                    left += 1
                
                count += i - left + 1

            return count

        return helper(goal) - helper(goal - 1)