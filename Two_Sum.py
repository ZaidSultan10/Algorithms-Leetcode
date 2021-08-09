class Solution:

    def two_sum(self, num1, target):

        for i in range(0, len(num1)):
            for j in range(i + 1, len(num1)):
                if (num1[i] + num1[j]) == target:
                    print(i, j)


obj1 = Solution()
obj1.two_sum([1, 2, 3, 4], 6)
