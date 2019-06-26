def self_dividing_numbers(left, right)
    (left..right).select{ |i| isValid(i)}
end

def isValid(n)
    n.digits.all?{ |digit| digit != 0 && n % digit == 0}
end