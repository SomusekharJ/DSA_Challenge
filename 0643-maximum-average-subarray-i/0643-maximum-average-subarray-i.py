class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        current_sum = sum(nums[:k])
        maximum_sum = current_sum
        for i in range(k,n):
            current_sum = current_sum + nums[i] - nums[i - k]
        
            if current_sum > maximum_sum:
                maximum_sum = current_sum
        
        return maximum_sum/k
        