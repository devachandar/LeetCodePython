# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findMatches(self, w1:str, w2:str):
        count = 0
        for i in range(6):
            if w1[i] == w2[i]:
                count+=1
        return count

    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        candidates = [*words]
        
        while candidates !=[]:
            word = candidates[random.randint(0,len(candidates)-1)]
            match = master.guess(word)
            if (match == 6):
                return
            temp = []
            for w in candidates:
                if (self.findMatches(w,word) == match):
                    temp.append(w)
            
            candidates = [*temp]