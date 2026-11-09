class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        max_value = 0
        distinct = set()
        left = 0
        currsum = 0
        for right in range(len(nums)):

            while nums[right] in distinct:
                distinct.remove(nums[left])
                currsum -= nums[left]
                left += 1

            distinct.add(nums[right])
            currsum += nums[right]
            max_value = max(max_value,currsum)
        
        return max_value

                

        