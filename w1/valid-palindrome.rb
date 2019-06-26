#Utilized regular expression and one-liner
def is_palindrome(s)
    s = s.downcase.split("").select{ |c| c =~ /[a-z0-9]/}
    s == s.reverse
end

#Normal approach
def is_palindrome(s)
    s = s.downcase.split("").select{ |c| c =~ /[a-z0-9]/}
    i, j = 0, s.length - 1
    while i < j
        return false if s[i] != s[j]
        i += 1
        j -= 1
    end
    true
end