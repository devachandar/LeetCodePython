class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:
            if stack:
                pop_ch = stack.pop()
                if pop_ch != ch:
                    stack.append(pop_ch)
                    stack.append(ch)
                    # print(stack)
            else:
                stack.append(ch)

        return "".join(stack)