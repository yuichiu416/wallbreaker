def binary_gap(n)
    n = n.to_s(2)
    max = 0
    dist = 0
    for i in 0...n.length
        if n[i] == "1"
            max = dist if dist > max
            dist = 1
        else
            dist += 1
        end
    end
    max 
end