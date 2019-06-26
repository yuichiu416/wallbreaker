#Ruby one-liner
def reverse_string(s)
    s.reverse!
end


#Normal approach
def reverse_string(s)
    return s if s.length <= 1
    i, j = 0, s.length - 1
    while i < j
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    end
end