def reverse_vowels(s)
    return s if s.length <= 1
    vowels = "aeiouAEIOU"
    i, j = 0, s.length - 1
    while i < j
        while i < s.length && !vowels.include?(s[i])
            i += 1
        end
        while j > 0 && !vowels.include?(s[j])
            j -= 1
        end
        break if i >= j
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    end
    s
end