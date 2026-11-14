class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        total = 0
        for i in range(len(grumpy)):
            if grumpy[i] != 1:
                total += customers[i]

        currsum = 0    
        for i in range(minutes):
            if grumpy[i] != 0:
                currsum += customers[i]
        
        maxsum = currsum
        for i in range(minutes,len(customers)):
            currsum += customers[i] * grumpy[i]
            currsum -= customers[i - minutes] * grumpy[i - minutes]
            maxsum = max(maxsum,currsum)

        return total + maxsum


