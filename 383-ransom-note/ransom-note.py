class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_ransomNote = Counter(ransomNote)
        freq_magazine = Counter(magazine)

        for freq in freq_ransomNote:
            if freq_ransomNote[freq] > freq_magazine[freq]:
                return False
        return True