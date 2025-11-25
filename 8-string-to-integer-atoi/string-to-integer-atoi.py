class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        num = 0
        positive = True
        print("ss", s.strip())
        s = s.strip()
        if s == "":
            return 0
        if s[0] == "-":
            positive = False
            s = s[1:]
        elif s[0] == "+":
            positive = True
            s = s[1:]
        for ch in s:
            print(ch)
            # if (ch == " "):
            #     continue
            # if ch == "-":
            #     positive = False
            #     continue
            if ch.isdigit():
                print(ch,"a")
                num = num*10 + int(ch)
            else:
                break
        
        if positive:
            if num > INT_MAX:
                return INT_MAX
            else:
                return num
        else:
            if -1 * num < INT_MIN:
                return INT_MIN
            else:
                return -1 * num