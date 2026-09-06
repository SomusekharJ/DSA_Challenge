class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        current_vowels = 0
        vowels = set("aeiou")
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels

        for j in range(k,n):
            if max_vowels == k:
                return max_vowels
            
            if s[j] in vowels:
                current_vowels += 1
            
            if s[j-k] in vowels:
                current_vowels -= 1
            
            if current_vowels > max_vowels:
                max_vowels = current_vowels

        return  max_vowels



            


        