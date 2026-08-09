class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        window_size = 2 * k + 1

        if window_size > n:
            return ans

        window_sum = sum(nums[:window_size])
        ans[k] = window_sum // window_size
        for i in range(k+1,n-k):
            window_sum -= nums[i-k-1]
            window_sum += nums[i+k]
            ans[i] = window_sum // window_size
        
        return ans