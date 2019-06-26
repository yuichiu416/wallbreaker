#Ruby one-liner
def hamming_distance(x, y)
    (x^y).to_s(2).count('1')
end

#Normal approach 
def hamming_distance(x, y)
    x, y = y, x if x > y
    binaryX = x.to_s(2)
    binaryY = y.to_s(2)
    #make the two arrays the same length
    (binaryY.length - binaryX.length).times{ binaryX = "0" + binaryX}
    ans = 0
    for i in 0...binaryX.length
        ans += 1 if binaryX[i] != binaryY[i]
    end
    ans
end
