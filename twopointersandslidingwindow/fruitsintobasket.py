class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l = 0
        fruit_count = {}
        maxi = 0

        for r in range(len(fruits)):
            fruit_count[fruits[r]] = fruit_count.get(fruits[r], 0) + 1
            while len(fruit_count) > 2:
                fruit_count[fruits[l]] -= 1
                if fruit_count[fruits[l]] == 0:
                    del fruit_count[fruits[l]]
                l += 1
            maxi = max(maxi, r - l + 1)
        return maxi

