from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        remaining = matrix

        while remaining:
            result += remaining[0]
            remaining = list(zip(*remaining[1:]))[::-1]

        return result
