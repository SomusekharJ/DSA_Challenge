class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def helper(x):
            if x < 0 : return 0

            binary = []
            for i in range(len(nums)):
                binary.append(nums[i] % 2)

            count = 0
            left = 0
            currsum = 0
            for i in range(len(binary)):
                currsum += binary[i]

                while currsum > x:
                    currsum -= binary[left]
                    left += 1
                    
                count += (i - left + 1)

            return count

        return helper(k) - helper(k - 1)

        
                

                

        