def numOfIslands(grid) -> int:
    ROWS = len(grid)
    COLS = len(grid[0])
    res = 0

    def dfs(r, c):
        if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == "0":
            return
        grid[r][c] = "0"

        lst = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
        for row, col in lst:
            dfs(row, col)

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                dfs(r, c)
                res += 1
    return res

grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
] # 3

grid2 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] # 1

print(numOfIslands(grid1))
print(numOfIslands(grid2))
