class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximumsubarray  = sum(nums[:k])
        currentsubarray = maximumsubarray
        for i in range(k,len(nums)):
            currentsubarray += nums[i] - nums[i - k]
            maximumsubarray = max(currentsubarray,maximumsubarray)
        return maximumsubarray/k      