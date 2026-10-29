class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        currsum = 0
        ans = float("inf")
        left = 0
        for right in range(len(nums)):
            currsum += nums[right]

            while currsum >= target:
                ans = min(ans, right - left + 1)
                currsum -= nums[left]
                left += 1
        
        return ans if ans != float("inf") else 0
