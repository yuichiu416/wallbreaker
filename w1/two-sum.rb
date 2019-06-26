#Ruby one-liner

def two_sum(nums, target)
    hash = Hash.new
    nums.each.with_index{ |num, i| hash[num] ? (return [hash[num], i]) : hash[target - num] = i}
end

#Or be more descriptive:
def two_sum(nums, target)
    hash = Hash.new
    nums.each.with_index do |num, i|
        if hash[num]
            return [hash[num], i]
        else
            # memorize the number we found
            hash[target - num] = i
        end
    end
end