class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_length = 0
        left = 0
        fruit_count = {}
        for right in range(len(fruits)):
            current_fruit = fruits[right]
            fruit_count[current_fruit] = fruit_count.get(current_fruit, 0) + 1 
            
            while len(fruit_count) > 2:
                current_left = fruits[left]
                fruit_count[current_left] -= 1 
                left += 1

                if fruit_count[current_left] == 0:
                    del fruit_count[current_left]
            
            max_length = max(max_length,right - left + 1)
        
        return max_length
