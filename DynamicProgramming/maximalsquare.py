
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]  # Memoization table
        max_side = 0  # To keep track of the largest square found
        max_side = [0]
        def findMaxSquare(i, j):
            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if matrix[i][j] == '0':
                dp[i][j] = 0
                return dp[i][j]

            top = findMaxSquare(i - 1, j)
            left = findMaxSquare(i, j - 1)
            diagonal = findMaxSquare(i - 1, j - 1)

            dp[i][j] = 1 + min(top, left, diagonal)

            max_side[0] = max(max_side[0], dp[i][j])

            return dp[i][j]

        for i in range(rows):
            for j in range(cols):
                findMaxSquare(i, j)

        return max_side[0] * max_side[0]


