class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                result = stack.pop() + stack.pop()
                stack.append(result)
    
            elif token == "-":
                sec = stack.pop()
                first = stack.pop()
                stack.append(first - sec)

            elif token == "*":
                result = stack.pop() * stack.pop()
                stack.append(result)

            elif token == "/":
                sec = stack.pop()
                first = stack.pop()
                stack.append(int(first / sec))
            else:
                stack.append(int(token))

        return stack[0]