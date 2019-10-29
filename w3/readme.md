Greedy algorithms


[860. Lemonade Change](https://leetcode.com/problems/lemonade-change)
```ruby
def lemonade_change(bills)
    fives, tens = 0, 0
    bills.each do |bill|
        case bill
            when 5
                fives += 1
            when 10
                fives -= 1
                tens += 1
            else
                if tens > 0
                    tens -= 1
                    fives -= 1
                else
                    fives -= 3
                end
        end
        return false if fives < 0 || tens < 0
    end
    true
end
```


[455. Assign Cookies](https://leetcode.com/problems/assign-cookies)
```ruby
def find_content_children(g, s)
    g.sort!
    s.sort!
    gi = g.length - 1
    si = s.length - 1
    ans = 0
    while gi >= 0 && si >= 0
        if s[si] >= g[gi]
            ans += 1
            gi -= 1
            si -= 1
        else 
            gi -= 1
        end
    end
    ans
end
```


[392. Is Subsequence](https://leetcode.com/problems/is-subsequence)
```ruby
def is_subsequence(s, t)
    si, ti = 0, 0
    return true if s.length == 0
    return false if t.length == 0
    match = ""
    while si < s.length && ti < t.length
        if s[si] == t[ti]
            match += s[si]
            si += 1
            ti += 1
        else
            ti += 1
        end
    end
    match == s
end
```

[452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons)
```ruby
def find_min_arrow_shots(points)
    return 0 if points.length == 0
    points.sort_by!{ |arr| arr[1]}
    arrowCount = 1
    arrowPos = points[0][1]
    
    for i in 0...points.length
        next if arrowPos >= points[i][0]
        arrowCount += 1
        arrowPos = points[i][1]
    end
    arrowCount
end
```

[763. Partition Labels](https://leetcode.com/problems/partition-labels)

Binary search


[704. Binary Search](https://leetcode.com/problems/binary-search)


[852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array)

Sorting


[242. Valid Anagram](https://leetcode.com/problems/valid-anagram)


[561. Array Partition I](https://leetcode.com/problems/array-partition-i)


[56. Merge Intervals](https://leetcode.com/problems/merge-intervals)

Use sorting, not a multiset (you solved this problem using a multiset last week) 
[438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string)

Recursion and memoization: make sure you use memoization if applicable for the problems below


[50. Pow(x, n)](https://leetcode.com/problems/powx-n)


[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)


[72. Edit Distance](https://leetcode.com/problems/edit-distance)


[213. House Robber II](https://leetcode.com/problems/house-robber-ii)

Do not use a built-in regex for this one: 
[10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

Dynamic Programming: same problems as above, but use dynamic programming this time


[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)


[72. Edit Distance](https://leetcode.com/problems/edit-distance)


[213. House Robber II](https://leetcode.com/problems/house-robber-ii)

Do not use a built-in regex for this one: 
[10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)