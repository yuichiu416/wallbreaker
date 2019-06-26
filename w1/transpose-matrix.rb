# Ruby one-liner
def transpose(a)
    a.transpose  #
end


# Normal approach
def transpose(a)
    ans = Array.new(a[i].length) {Array.new(a.length, [])}

    for i in 0...a.legnth
        for j in 0...a[i].length
            ans[j][i] = a[i][j]
        end
    end
    ans
end
