#Ruby one-liner
def plus_one(digits)
    (digits.join("").to_i + 1).digits.reverse
end

#Normal approach
def plus_one(digits)
    digits[-1] += 1
    done = false
    i = digits.length - 1
    while !done
        done = true
        if digits[i] == 10
            done = false
            digits[i] = 0
            if i > 0
                digits[i - 1] += 1
            else
                digits.unshift(1)
                return digits
            end
        end
        i -= 1
    end
    digits
end