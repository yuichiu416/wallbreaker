# Ruby one-liner

def is_anagram(s, t)
    s.split("").sort == t.split("").sort
end

# Normal approach
def is_anagram(s, t)
    hash1 = Hash.new(0)
    hash2 = Hash.new(0)
    s.each_char{ |c| hash1[c] += 1}
    t.each_char{ |c| hash2[c] += 1}
    hash1 == hash2
end