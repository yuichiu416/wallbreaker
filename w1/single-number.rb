def single_number(nums)
    hash = Hash.new(0)
    nums.each{ |ele| hash[ele] += 1}
    hash.key(1)
end