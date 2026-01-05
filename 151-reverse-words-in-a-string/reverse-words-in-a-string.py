class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split() # split words into string, remove extra spaces
        reversed_words = words[::-1] # reverse the list of words
        return ' '.join(reversed_words) # join them back in space
        
        # output = ''
        # s = s.strip()
        # right = len(s)
        # for left in range(len(s)-1,-1,-1):
        #     if (s[left]== ' ' and s[left-1] != ' '):
        #         output+=s[left+1:right].strip()+" "
        #         right = left
        
        # output+= s[0:right]
        # return output.strip()
