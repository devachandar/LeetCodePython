class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = self.get_next(n)

        return n == 1

    def get_next(self, n: int) -> int:
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total
        # total_sum = 0
        # while n > 9:
        #     num = n
        #     total_sum = 0
        #     while num > 0:
        #         total_sum += (num % 10) ** 2  # Extract the last digit
        #         num //= 10             # Remove the last digit
        #     print(total_sum)
        #     n = total_sum

        # if n < 10:
        #     if n == 1:
        #         return True
        #     else:
        #         return False
        