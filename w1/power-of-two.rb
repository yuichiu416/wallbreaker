def is_power_of_two(n)
    return false if n < 1
    while n > 1
        return false if n % 2 != 0 || n % 1 != 0
        n /= 2
    end
    true
end