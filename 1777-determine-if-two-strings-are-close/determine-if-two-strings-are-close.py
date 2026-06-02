class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq_word1 = Counter(word1)
        freq_word2 = Counter(word2)

        word1_freq_list = []
        word2_freq_list = []


        for val in freq_word1:
            word1_freq_list.append(freq_word1[val])
        for val in freq_word2:
            word2_freq_list.append(freq_word2[val])

        print(word1_freq_list, word2_freq_list)
        return (
            set(freq_word1.keys()) == set(freq_word2.keys()) and 
            sorted(word1_freq_list) == sorted(word2_freq_list)
        )