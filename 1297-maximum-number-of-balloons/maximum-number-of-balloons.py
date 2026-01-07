class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
       
        freq = {'b':0,'a':0,'l':0,"o":0,"n":0}
        for i in text:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i]+=1
        return min(freq['b'],freq['a'],int(freq['l'] / 2),int(freq['o'] / 2),freq['n'])



        # freq = Counter(text)
        # freq = 'b':0,'a':0,'l':0,"o":0,"n":0}
        # for i in text:
        #     if i not in freq:
        #         freq[i] = 1
        #     else:
        #         freq[i]+=1
        # return min(freq['b'],freq['a'],int(freq['l'] / 2),int(freq['o'] / 2),freq['n'])