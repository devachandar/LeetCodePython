class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        diff = [0] * 101   # years 1950-2050

        for birth, death in logs:
            diff[birth - 1950] += 1
            diff[death - 1950] -= 1

        population = 0
        max_population = 0
        answer = 1950

        for i in range(101):
            population += diff[i]

            if population > max_population:
                max_population = population
                answer = 1950 + i

        return answer