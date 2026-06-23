class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures) 

        for i in range(len(temperatures)):
            # count = 0
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # count +=1
                idx = stack.pop()
                result[idx] = i - idx
            
            stack.append(i)

        return result