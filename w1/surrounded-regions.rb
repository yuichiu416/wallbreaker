def solve(board)
    return board if board.empty? || board.length < 2 || board[0].empty? ||board[0].length < 2

    m = board.length
    n = board[0].length

    for i in 0...m
        for j in 0...n
            # start from the edge, mark all connected "O" to "*"
            dfs(board, i, j, m, n) if board[i][j] == "O" && isEdge(i, j, m, n)
        end
    end
    
    for i in 1...m - 1
        for j in 1...n - 1
            # mark all "O" to "X"
            board[i][j] = "X" if board[i][j] == "O"
        end
    end
    for i in 0...m
        for j in 0...n
            # mark the "O" that connected to the edge back
            board[i][j] = "O" if board[i][j] == "*"
        end
    end
end

def dfs(board, i, j, m, n)
    return if i < 0 || i >= m || j < 0 || j >= n
    board[i][j] = "*" if board[i][j] == "O"
    
    dfs(board, i + 1, j, m, n) if i + 1 < m && board[i + 1][j] == "O"
    dfs(board, i - 1, j, m, n) if i - 1 > 0 && board[i - 1][j] == "O"
    dfs(board, i, j + 1, m, n) if j + 1 < n && board[i][j + 1] == "O"
    dfs(board, i, j - 1, m, n) if j - 1 > 0 && board[i][j - 1] == "O"
end

def isEdge(i, j, m, n)
    return true if i == 0 || j == 0 || i == m - 1 || j == n - 1
    false
end