class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        counter = 0
        new_str = ""
        
        while counter < len(word1) or counter < len(word2):
            if counter < len(word1):
                new_str+=word1[counter]
            if counter < len(word2):
                new_str+=word2[counter]
            counter+=1
        
        return new_str

