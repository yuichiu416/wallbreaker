#Ruby one-liner
def reverse_words(s)
    s.split(" ").map(&:reverse).join(" ")
end