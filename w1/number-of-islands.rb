def num_islands(grid)
    return 0 if grid.length < 1
    m = grid.length
    n = grid[0].length
    ctr = 0
    for i in 0...m
        for j in 0...n
            if grid[i][j] == '1'
                # all the previous islands will be removed, the new 1's will be a new island
                dfs(grid, i, j, m, n)
                ctr += 1
            end
        end
    end
    ctr
end

def dfs(grid, i, j, m, n)
    return if i < 0 || i == m || j < 0 || j == n || grid[i][j] != "1"
    # clear the island we found
    grid[i][j] = 0
    dfs(grid, i + 1, j, m, n)
    dfs(grid, i - 1, j, m, n)
    dfs(grid, i, j + 1, m, n)
    dfs(grid, i, j - 1, m, n)
end