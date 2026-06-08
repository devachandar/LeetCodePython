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


        # n = len(word1)
        # m = len(word2)
        # left = 0
        # right = 0
        # new_str = ""
        # while left < n or right < m:
        #     if left < n :
        #         new_str += word1[left]
        #         left +=1
        #     if right < m:
        #         new_str += word2[right]
        #         right +=1


        # return new_str 