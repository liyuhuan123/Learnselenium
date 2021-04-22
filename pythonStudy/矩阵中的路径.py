# 链接：https://www.nowcoder.com/practice/2a49359695a544b8939c77358d29b7e6?tpId=13&tqId=11218&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tab=answerKey
class Solution:
    def hasPath(self, matrix, word):
        row = len(matrix)
        col = len(matrix[0])
        visited = [[False for i in range(col)] for j in range(row)]
        if row == 0:
            return False
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == word[0]:
                    if self.dfs(matrix, row, col, i, j, 0, word, visited):
                        return True
        return False
    def dfs(self, matrix, row, col, x, y, index, word, visited):
        if index == len(word) - 1:
            return word[index] == matrix[x][y]
        nextX = [-1, 1, 0, 0]
        nextY = [0, 0, 1, -1]
        if matrix[x][y] == word[index]:
            visited[x][y] = True
            for i in range(4):
                newX = nextX[i] + x
                newY = nextY[i] + y
                if 0 <= newX < row and newY >= 0 and newY < col and visited[newX][newY] == False:
                    if self.dfs(matrix, row, col, newX, newY, index + 1, word, visited):
                        return True

            visited[x][y] = False
        return False