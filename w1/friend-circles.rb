def find_circle_num(m)
    visited = Array.new(m.length, false)
    circle = 0
    for i in 0...m.length
        for j in 0...m[i].length
            if !visited[i] && m[i][j] == 1
                dfs(m, visited, i)
                circle += 1
            end
        end
    end
    circle
end

def dfs(m, visited, i)
    visited[i] = true
    for j in 0...m.length
        if !visited[j] && m[i][j] == 1
            dfs(m, visited, j)
        end
    end
end