class Solution:
    def generateRow(self, row):
        ans = 1
        ansrow = [1]

        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ansrow.append(ans)

        return ansrow


    def generate(self, numRows):
        ans = []

        for i in range(1, numRows + 1):
            ans.append(self.generateRow(i))

        return ans