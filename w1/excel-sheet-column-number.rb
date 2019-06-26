def title_to_number(s)
    arr = [0] + ("A".."Z").to_a
    sum = 0
    i = 0
    while i < s.length
        sum += 26 ** i * arr.index(s[-i - 1])
        i += 1
    end
    sum
end