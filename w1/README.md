## wallbreaker-w1
### week 1 assignments

[905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)

[sort-arra-by-parity.rb](./sort-arra-by-parity.rb)
```
def sort_array_by_parity(a)
    return [] if a.length < 1
    left, right = 0, a.length - 1
    while left < right
        while left < a.length - 1 && a[left].even?
            left += 1
        end
        while right > 0 && a[right].odd?
            right -= 1
        end
        break if left >= right
        a[left], a[right] = a[right], a[left]
        left += 1
        right -= 1
    end
    a
end
```

---
[867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)

[transpose-matrix.rb](./transpose-matrix.rb)

**Ruby one-liner**
```
def transpose(a)
    a.transpose  #
end
```

**Normal approach**
```
def transpose(a)
    ans = Array.new(a[i].length) {Array.new(a.length, [])}

    for i in 0...a.legnth
        for j in 0...a[i].length
            ans[j][i] = a[i][j]
        end
    end
    ans
end
```

---
[832. Flipping an Image](https://leetcode.com/problems/flipping-an-image/)

[flipping-an-image.rb](./flipping-an-image.rb)

**Ruby one-liner**

```
def flip_and_invert_image(a)
   a.map(&:reverse).map { |row| row.map { |ele| ele == 1? 0 : 1} }
end
```

**Normal approach**
```
def flip_and_invert_image(a)
    a.each.with_index do |row, i|
        a[i] = row.reverse.map { |ele| ele == 1? 0:1}
    end
    a
end
```

---
[728. Self Dividing Numbers](https://leetcode.com/problems/self-dividing-numbers/)

[self-dividing-numbers.rb](./self-dividing-numbers.rb)

**Ruby one-liner**

```
def self_dividing_numbers(left, right)
    (left..right).select{ |i| isValid(i)}
end

def isValid(n)
    n.digits.all?{ |digit| digit != 0 && n % digit == 0}
end
```

---
[412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)

[fizz-buzz.rb](./fizz-buzz.rb)

```
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
```

---
[66. Plus One](https://leetcode.com/problems/plus-one/)

[plus-one.rb](./plus-one.rb)

**Ruby one-liner**

```
def plus_one(digits)
    (digits.join("").to_i + 1).digits.reverse
end
```

**Normal approach**
```
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
```

---
[171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

[excel-sheet-column-number.rb](./excel-sheet-column-number.rb)
```
def title_to_number(s)
    arr = [0] + ("A".."Z").to_a
    sum = 0
    i = 0
    while i < s.length
        sum += 26 ** i * arr.index(s[-i - 1])
        i += 1
    end
    sum
end
```

---
[231. Power of Two](https://leetcode.com/problems/power-of-two/)

[power-of-two.rb](./power-of-two.rb)

```
def is_power_of_two(n)
    return false if n < 1
    while n > 1
        return false if n % 2 != 0 || n % 1 != 0
        n /= 2
    end
    true
end
```

---
[344. Reverse String](https://leetcode.com/problems/reverse-string/)

[reverse-string.rb](./reverse-string.rb)

**Ruby one-liner**

```
def reverse_string(s)
    s.reverse!
end
```

**Normal approach**
```
def reverse_string(s)
    return s if s.length <= 1
    i, j = 0, s.length - 1
    while i < j
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    end
end
```

---
[520. Detect Capital](https://leetcode.com/problems/detect-capital/)

[detect-capital.rb](./detect-capital.rb)

```
def detect_capital_use(word)
    word == word.upcase || word == word.downcase || word == word.capitalize
end
```

---
[557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

[reverse-words-in-a-string-iii.rb](./reverse-words-in-a-string-iii.rb)

**Ruby one-liner**
```
def reverse_words(s)
    s.split(" ").map(&:reverse).join(" ")
end
```

---
[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

[valid-palindrome](./valid-palindrome)

**Ruby one-liner**
```
def is_palindrome(s)
    s = s.downcase.split("").select{ |c| c =~ /[a-z0-9]/}
    s == s.reverse
end
```

**Normal approach**
```
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
```

---
[345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

[reverse-vowels-of-a-string.rb](./reverse-vowels-of-a-string.rb)

```
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
```

---
[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

[longest-common-prefix.rb](./longest-common-prefix.rb)

```
def longest_common_prefix(strs)
    ans = ""
    return "" if strs.empty? || strs[0].empty?
    for i in 0...strs[0].length
        ans << strs[0][i] if strs.all?{ |str| str.start_with?(strs[0][0..i])}
    end
    ans 
end
```

---
[476. Number Complement](https://leetcode.com/problems/number-complement/)

[number-complement.rb](./number-complement.rb)

```
def find_complement(num)
    arr = []
    # get binary value, or just use binary = num.to_s(2)
    while num >= 2
        arr.unshift(num % 2)
        num /= 2
    end
    arr.unshift(num)
    arr.map!{ |ele| ele == 0? 1 : 0}
    n = 0
    i = 0
    #calculate decimal value from binary value, or just use num = str.to_i(2)
    for i in 0...arr.length
        n += 2 ** i * arr[-i - 1]
    end
    n
end
```

---
[461. Hamming Distance](https://leetcode.com/problems/hamming-distance/)

[hamming-distance.rb](./hamming-distance.rb)

**Ruby one-liner**
```
def hamming_distance(x, y)
    (x^y).to_s(2).count('1')
end
```

**Normal approach**
```
def hamming_distance(x, y)
    x, y = y, x if x > y
    binaryX = x.to_s(2)
    binaryY = y.to_s(2)
    #make the two arrays the same length
    (binaryY.length - binaryX.length).times{ binaryX = "0" + binaryX}
    ans = 0
    for i in 0...binaryX.length
        ans += 1 if binaryX[i] != binaryY[i]
    end
    ans
end
```

---
[868. Binary Gap](https://leetcode.com/problems/binary-gap/)

[binary-gap.rb](./binary-gap.rb)
```
def binary_gap(n)
    n = n.to_s(2)
    max = 0
    dist = 0
    for i in 0...n.length
        if n[i] == "1"
            max = dist if dist > max
            dist = 1
        else
            dist += 1
        end
    end
    max 
end
```

---
[136. Single Number](https://leetcode.com/problems/single-number/)

[single-number.rb](./single-number.rb)

```
def single_number(nums)
    hash = Hash.new(0)
    nums.each{ |ele| hash[ele] += 1}
    hash.key(1)
end
```

---
[1. Two Sum](https://leetcode.com/problems/two-sum/)

[two-sum.rb](./two-sum.rb)

**Ruby one-liner**

```
def two_sum(nums, target)
    hash = Hash.new
    nums.each.with_index{ |num, i| hash[num] ? (return [hash[num], i]) : hash[target - num] = i}
end
```

Or be more descriptive:
```
def two_sum(nums, target)
    hash = Hash.new
    nums.each.with_index do |num, i|
        if hash[num]
            return [hash[num], i]
        else
            # memorize the number we found
            hash[target - num] = i
        end
    end
end
```

---
[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)

[valid-anagram.rb](./valid-anagram.rb)

**Ruby one-liner**
```
def is_anagram(s, t)
    s.split("").sort == t.split("").sort
end
```

**Normal approach**
```
def is_anagram(s, t)
    hash1 = Hash.new(0)
    hash2 = Hash.new(0)
    s.each_char{ |c| hash1[c] += 1}
    t.each_char{ |c| hash2[c] += 1}
    hash1 == hash2
end
```

---
[547. Friend Circles](https://leetcode.com/problems/friend-circles/)

[friend-circles.rb](./friend-circles.rb)


```
def find_circle_num(m)
    visited = Array.new(m.length, false)
    circle = 0
    for i in 0...m.length
        for j in 0...m[i].length
            if !visited[i] && m[i][j] == 1
                dfs(m, visited, i)
                circle += 1
            end
        end
    end
    circle
end

def dfs(m, visited, i)
    visited[i] = true
    for j in 0...m.length
        if !visited[j] && m[i][j] == 1
            dfs(m, visited, j)
        end
    end
end
```

---
[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

[number-of-islands.rb](./number-of-islands.rb)

```
def num_islands(grid)
    island = 0
    return 0 if grid.empty?
    m = grid.length
    n = grid[0].length
    for i in 0...m
        for j in 0...n
            if grid[i][j] == "1"
                dfs(grid, i, j, m, n)
                island += 1
            end
        end
    end
    island
end

def dfs(grid, i, j, m, n)
    grid[i][j] = "0"
    dfs(grid, i - 1, j, m, n) if i - 1 >= 0 && grid[i - 1][j] == "1"
    dfs(grid, i + 1, j, m, n) if i + 1 < m && grid[i + 1][j] == "1"
    dfs(grid, i, j - 1, m, n) if j - 1 >= 0 && grid[i][j - 1] == "1"
    dfs(grid, i, j + 1, m, n) if j + 1 < n && grid[i][j + 1] == "1"
end
```


---
[130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)

[surrounded-regions.rb](./surrounded-regions.rb)

```
def solve(board)
    return board if board.empty? || board.length < 2 || board[0].empty? ||board[0].length < 2
    m = board.length
    n = board[0].length
    for i in 0...m
        for j in 0...n
            next if !isEdge?(i, j, m, n)
            dfs(board, i, j, m, n) if board[i][j] == "O"
        end
    end
    
    for i in 0...m
        for j in 0...n
            next if isEdge?(i, j, m, n)
            board[i][j] = "X" if board[i][j] == "O"
        end
    end
    
    for i in 0...m
        for j in 0...n
            board[i][j] = "O" if board[i][j] == "*"
        end
    end
   board         
end

def dfs(board, i, j, m, n)
    board[i][j] = "*"
    
    dfs(board, i - 1, j, m, n) if i - 1 >= 0 && board[i - 1][j] == "O"
    dfs(board, i + 1, j, m, n) if i + 1 < m && board[i + 1][j] == "O"
    dfs(board, i, j - 1, m, n) if j - 1 >= 0 && board[i][j - 1] == "O"
    dfs(board, i, j + 1, m, n) if j + 1 < n && board[i][j + 1] == "O"
end

def isEdge?(i, j, m, n)
    i == 0 || j == 0 || i == m - 1 || j == n - 1
end
    
```