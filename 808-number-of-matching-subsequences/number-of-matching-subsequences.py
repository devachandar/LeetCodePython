class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        def is_sequence(word):
            temp = s
            for ch in word:
                idx = temp.find(ch)
                if idx == -1:
                    return False
                temp = temp[idx + 1:]
            return True


        for word in words:
            if is_sequence(word):
                count+=1
        
        return count

        # count = 0
        # s_freq = Counter(s)
        # for word in words:
        #     word_freq = Counter(word)
        #     for key in word_freq:
        #         if s_freq[key] < word_freq[key]:
        #             break      
        #     else:  
        #         count+=1
        
        # return count