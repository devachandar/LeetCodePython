class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # dp[i][j] = s[0:i] matches p[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True   # empty string matches empty pattern
        
        # Handle patterns like a*, a*b*, .* , c*a*b*
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                if p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                
                elif p[j - 1] == '*':
                    # Option 1: skip x* => dp[i][j-2]
                    dp[i][j] = dp[i][j - 2]
                    
                    # Option 2: use x* if matches
                    if p[j - 2] in {s[i - 1], '.'}:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]
