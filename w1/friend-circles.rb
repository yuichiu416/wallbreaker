def find_circle_num(m)
    circle = 0
    visited = Array.new(m.length, 0)
    for i in 0...m.length
        # find friends from self, each person himself can be a new circle if he's not connected to everyone
        if visited[i] == 0
            dfs(m, visited, i)
            circle += 1
        end
    end
    circle
end

def dfs(m, visited, i)
    for j in 0...m.length
        # find based on the previous person's friend cycle
        if m[i][j] == 1 && visited[j] == 0
            visited[j] = 1
            dfs(m, visited, j)
        end
    end
end