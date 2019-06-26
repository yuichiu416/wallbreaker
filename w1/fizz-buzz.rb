def fizz_buzz(n)
    ans = []
    (1..n).each do |ele|
        if ele % 3 == 0 && ele % 5 == 0
            ans << "FizzBuzz"
        elsif ele % 3 == 0
            ans << "Fizz"
        elsif ele % 5 == 0
            ans << "Buzz"
        else
            ans << ele.to_s
        end
    end
    ans
end