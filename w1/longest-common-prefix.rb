def longest_common_prefix(strs)
    ans = ""
    return "" if strs.empty? || strs[0].empty?
    for i in 0...strs[0].length
        ans << strs[0][i] if strs.all?{ |str| str.start_with?(strs[0][0..i])}
    end
    ans 
end