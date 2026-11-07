class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = float("inf")
        left = 0
        currsum = 0
        for right in range(len(nums)):
            currsum += nums[right]

            while currsum >= target:
                ans = min(ans,right - left + 1)
                currsum -= nums[left]
                left += 1
        
        return ans if ans != float("inf") else 0

        