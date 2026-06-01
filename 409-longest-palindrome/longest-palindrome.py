class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
        freq_s = Counter(s)
        count = 0
        flag = False

        for val in freq_s:
            if freq_s[val] % 2 == 0:
                count+= freq_s[val]
            else:
                count += int(freq_s[val]/2) * 2
                # if int(freq_s[val]/2) == 0 or int(freq_s[val]/2) == 1:
                flag= True

        if flag:
            count+=1

        return count
 