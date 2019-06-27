def num_islands(grid)
    return 0 if grid.length < 1
    island = 0
    return 0 if grid.empty?
    m = grid.length
    n = grid[0].length
    for i in 0...m
        for j in 0...n
            if grid[i][j] == "1"
                dfs(grid, i, j, m, n)
                island += 1
            end
        end
    end
    island
end

def dfs(grid, i, j, m, n)
    grid[i][j] = "0"
    dfs(grid, i - 1, j, m, n) if i - 1 >= 0 && grid[i - 1][j] == "1"
    dfs(grid, i + 1, j, m, n) if i + 1 < m && grid[i + 1][j] == "1"
    dfs(grid, i, j - 1, m, n) if j - 1 >= 0 && grid[i][j - 1] == "1"
    dfs(grid, i, j + 1, m, n) if j + 1 < n && grid[i][j + 1] == "1"
end