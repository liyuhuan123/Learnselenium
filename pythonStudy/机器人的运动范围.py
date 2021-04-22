def movingCount(self, threshold, rows, cols):
    if rows < 1 or cols < 1 or threshold < 0:
        return 0
    visited = [False] * (rows * cols)
    return self.moving(threshold, rows, cols, 0, 0, visited)


def moving(self, threshold, rows, cols, curx, cury, visited):
    cnt = 0
    if 0 <= curx < cols and 0 <= cury < rows and not visited[cury * cols + curx]:
        if self.calbitsum(curx) + self.calbitsum(cury) <= threshold:
            visited[cury * cols + curx] = True
            # 能到达格子数为当前位置+四个方向能走到的格子数总和
            cnt = 1 + self.moving(threshold, rows, cols, curx - 1, cury, visited) \
                  + self.moving(threshold, rows, cols, curx, cury - 1, visited) \
                  + self.moving(threshold, rows, cols, curx + 1, cury, visited) \
                  + self.moving(threshold, rows, cols, curx, cury + 1, visited)
    return cnt


def calbitsum(self, x):
    ressum = 0
    while x != 0:
        ressum += x % 10
        x /= 10
    return ressum
