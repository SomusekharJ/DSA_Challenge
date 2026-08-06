class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        currentvowels = 0
        maxvowels = 0
        vowels = set("aeiou")
        for i in range(k):
            if s[i] in vowels:
                currentvowels += 1
        maxvowels = max(currentvowels,maxvowels)

        for i in range(k,len(s)):
            if s[i] in vowels:
                currentvowels += 1

            if s[i-k] in vowels:
                currentvowels -= 1
            
            maxvowels = max(currentvowels,maxvowels)
        return maxvowels
        