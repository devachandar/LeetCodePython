class Solution:
    def reverseWords(self, s: str) -> str:
        output = ''
        # right = len(s)
        s = s.strip()
        right = len(s)
        print(s,"d")
        for left in range(len(s)-1,-1,-1):
            if (s[left]== ' ' and s[left-1] != ' '):
                output+=s[left+1:right].strip()+" "
                print(output,"dd")
                right = left
        
        output+= s[0:right]
        return output.strip()
