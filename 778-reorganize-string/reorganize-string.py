class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)

        max_char = max(freq, key=freq.get)
        if freq[max_char] > (n + 1) // 2:
            return ""

        result = [""] * n
        idx = 0

        # Step 1: place most frequent character
        while freq[max_char] > 0:
            result[idx] = max_char
            idx += 2
            freq[max_char] -= 1

        # Step 2: place remaining characters
        # idx = 1
        for ch in freq:
            while freq[ch] > 0:
                if idx >= n:
                    idx = 1
                print(result)
                result[idx] = ch
                idx += 2
                freq[ch] -= 1

        return "".join(result)


        