class Solution:
    def reverse(self, x: int) -> int:
        print("dd",str(x))
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31 
        if x>0:
            # print("a",int(str(x)[::-1]))
            rev = int(str(x)[::-1])
            if rev > INT_MAX:
                return 0
            else:
                return rev
        elif x<0:
            rev = -1 * int(str(x)[:0:-1])
            if rev < INT_MIN:
                return 0
            else:
                return rev
        else:
            return 0