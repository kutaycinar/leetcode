from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min = salary[0]
        max = salary[0]
        sum = 0
        for n in salary:
            sum += n
            if n < min:
                min = n
            if n > max:
                max = n
        return (sum - (min + max)) / (len(salary) - 2)

# Time:  O(n)
# Space: O(1)
