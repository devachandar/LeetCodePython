class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_s = s.split()

        if len(pattern) != len(list_s):
            return False

        pattern_to_s = {}
        s_to_pattern = {}

        for i in range(len(pattern)):
            print(pattern[i],pattern_to_s,s_to_pattern,list_s[i])
            if pattern[i] in pattern_to_s and pattern_to_s[pattern[i]] != list_s[i]:
                return False
            
            if list_s[i] in s_to_pattern and s_to_pattern[list_s[i]] != pattern[i]:
                return False

            pattern_to_s[pattern[i]] = list_s[i] 
            s_to_pattern[list_s[i]] = pattern[i]

        return True