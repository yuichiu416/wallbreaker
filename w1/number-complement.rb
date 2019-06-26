def find_complement(num)
    arr = []
    # get binary value, or just use binary = num.to_s(2)
    while num >= 2
        arr.unshift(num % 2)
        num /= 2
    end
    arr.unshift(num)
    arr.map!{ |ele| ele == 0? 1 : 0}
    n = 0
    i = 0
    #calculate decimal value from binary value, or just use num = str.to_i(2)
    for i in 0...arr.length
        n += 2 ** i * arr[-i - 1]
    end
    n
end