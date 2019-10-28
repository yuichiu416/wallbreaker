## Hash maps and hash sets

[771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

```ruby
def num_jewels_in_stones(j, s)
    hash = {}
    j.each_char{ |c| hash[c] = 0}
    s.each_char{ |c| hash[c] += 1 if !hash[c].nil?}
    hash.values.sum
end
```

[804. Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/)
```ruby

def unique_morse_representations(words)
    return 0 if words.nil? || words.length == 0
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    letters = ("a".."z").to_a
    hash = {}
    
    words.each do |word|
        morsed_word = ""
        word.each_char{ |c| morsed_word += morse[letters.index(c)]}
        hash[morsed_word] = true
    end
    hash.values.length
end
```

[202. Happy Number](https://leetcode.com/problems/happy-number/)

```ruby
def is_happy(n)
   hash = Hash.new(0)
    while !hash.values.any?{ |v| v > 1}
        sum = 0
        n.digits.each{ |d| sum += d ** 2}
        return true if sum == 1
        n = sum
        hash[sum] += 1
    end
    false  
end
```

[884. Uncommon Words from Two sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/)

```ruby
def uncommon_from_sentences(a, b)
    hash = Hash.new(0)
    a.split(" ").each{ |word| hash[word] += 1}
    b.split(" ").each{ |word| hash[word] += 1}
    hash.select{ |k, v| v == 1}.keys
end
```

[575. Distribute Candies](https://leetcode.com/problems/distribute-candies/)

```ruby
def distribute_candies(candies)
    hash = {}
    candies.each{ |n| hash[n] = true}
    len = candies.length / 2
    [len, hash.keys.length].min
end
```

[893. Groups of Special-Equivalent Strings](https://leetcode.com/problems/groups-of-special-equivalent-strings/)

```ruby
def num_special_equiv_groups(a)
    hash = {}
    a.each do |str|
        chars = str.split("")
        odd = []
        even = []
        chars.each.with_index do |c, i|
            if i.even?
                even << c
            else
                odd << c
            end
        end
        hash[odd.sort + even.sort] = true
    end
    hash.keys.length
end
```

[349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

```ruby
def intersection(nums1, nums2)
    hash = {}
    ans = {}
    nums1.each{ |num| hash[num] = true}
    nums2.each{ |num| ans[num] = num if hash[num]}
    ans.values
end
```

[36. Valid Sudoko](https://leetcode.com/problems/valid-sudoku/)

```ruby
def is_valid_sudoku(board)
    check1(board) && check2(board) && check3(board)
end

def check1(board)
    board.each do |row|
        hash = Hash.new(0)
        row.each{ |ele| hash[ele] += 1 if ele != "."}
        return false if hash.values.any?{ |v| v > 1}
    end
    true
end

def check2(board)
    for i in 0...9
        hash = Hash.new(0)
        for j in 0...9
            cell = board[j][i]
            hash[cell] += 1 if cell != "."
        end
        return false if hash.values.any?{ |v| v > 1} 
    end
    true
end

def check3(board)
    sub_board_indices = [1,4,7]
    sub_board_indices.each do |row|
        sub_board_indices.each do |col|
            return false if !helper(board, row, col)
        end
    end
    true
end

def helper(board, row, col)
    indices = [-1, 0, 1]
    hash = Hash.new(0)
    indices.each do |i|
        indices.each do |j|
            cell = board[row + i][col + j]
            hash[cell] += 1 if cell != "." 
        end
    end
    hash.each.none?{ |k, v| k != "." && v > 1}
end
```

[205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

```ruby
def is_isomorphic(s, t)
    hash1 = Hash.new(0)
    hash2 = Hash.new(0)
    
    for i in 0...s.length
        return false if hash1[s[i]] != hash2[t[i]]
        hash1[s[i]] = i + 1
        hash2[t[i]] = i + 1
    end
    true
end
```

[209. W0rd Pattern](https://leetcode.com/problems/word-pattern/)

```ruby
def word_pattern(pattern, str)
    return false if pattern.nil? || str.nil?
    hash = {}
    words = str.split(" ")
    return false if pattern.length != words.length 
    for i in 0...pattern.length
        if hash[pattern[i]].nil?
            hash[pattern[i]] = words[i]
        else
            return false if hash[pattern[i]] != words[i]
        end
    end
    values = hash.values
    return false if values != values.uniq
    true
end
```

[706. Design HashMap](https://leetcode.com/problems/design-hashmap/)

```ruby
class MyHashMap

=begin
    Initialize your data structure here.
=end
    attr_accessor :key, :value, :next
    def initialize(key = nil,value = nil)
        @map = Array.new(1000001, -1)
    end


=begin
    value will always be non-negative.
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        @map[key] = value
    end


=begin
    Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        @map[key]
    end
=begin
    Removes the mapping of the specified value key if this map contains a mapping for the key
    :type key: Integer
    :rtype: Void
=end
    def remove(key)
        @map[key] = -1
    end


end
```

[705. Design HashSet](https://leetcode.com/problems/design-hashset/)

```ruby
class MyHashSet

=begin
    Initialize your data structure here.
=end
    def initialize()
        @set = Array.new(1000001, false)
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def add(key)
        @set[key] = true
    end


=begin
    :type key: Integer
    :rtype: Void
=end
    def remove(key)
        @set[key] = false
    end


=begin
    Returns true if this set contains the specified element
    :type key: Integer
    :rtype: Boolean
=end
    def contains(key)
        @set[key]
    end

end
```

## Multisets

[438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
```ruby
def find_anagrams(s, p)
    ans = []
    left, right = 0, p.length
    set = Hash.new(0)
    
    return ans if p.length > s.length
    
    if p.length == 1
        (0...s.length).each{ |i| ans << i if s[i] == p}
        return ans;
    end
    
    for i in 0...p.length
        set[p[i]] ||= 0
        set[p[i]] += 1
        set[s[i]] ||= 0
        set[s[i]] -= 1
    end
    
    while right < s.length
        ans << left if set.values.all?(&:zero?)
        c = s[left]
        set[c] += 1 if set.key?(c)
        c = s[right]
        set[c] -= 1 if set.key?(c)
        
        left += 1
        right += 1
    end
    
    ans << left if set.values.all?(&:zero?)
    ans
end
```

[387. First Unique Character ina String](https://leetcode.com/problems/first-unique-character-in-a-string/)

```ruby
def first_uniq_char(s)
    return -1 if s.empty?
    hash = Hash.new(0)
    s.each_char{ |c| hash[c] += 1}
    first_pair = hash.select{ |k, v| v == 1}.first
    if first_pair == nil
        return -1
    end
    c = first_pair[0]
    s.index(c)
end
```

[811. Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/)
```ruby
def subdomain_visits(cpdomains)
    hash = Hash.new(0)
    domains = [];
    cpdomains.each do |n|
        times, domain = n.split(" ")
        times = times.to_i
        subs = domain.split(".")
        for i in 0...subs.length
            #domains.push(subs[i..-1].join("."))
            hash[subs[i..-1].join(".")] += times
        end
    end
    hash.to_a.map(&:reverse).map{ |str| str.join(" ")}
end
```

[389. Find the Difference](https://leetcode.com/problems/find-the-difference/)
```ruby
def find_the_difference(s, t)
    hash = Hash.new(0)
    s.each_char{ |c| hash[c] += 1}
    t.each_char{ |c| hash[c] -= 1}
    hash.each{ |k, v| return k if v == -1 }
end
```

[819. Most Common Word](https://leetcode.com/problems/most-common-word/)
```ruby
def most_common_word(paragraph, banned)
    hash = Hash.new(0)
    paragraph.split(/\W/).each{ |word| hash[word.downcase] += 1}
    selected = hash.select{ |k, v| !banned.include?(k) && k.length > 0}
    selected.sort_by{ |k, v| v}[-1][0]
end
```

[451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)
```ruby
def frequency_sort(s)
    hash = Hash.new(0)
    s.each_char{ |c| hash[c] += 1}
    hash = hash.sort_by{ |k, v| v }.reverse
    ans = ""
    hash.each{ |c, times| ans += c * times}
    ans
end
```

[645. Set Mismatch](https://leetcode.com/problems/set-mismatch/)
```ruby
def find_error_nums(nums)
    arr = Array.new(nums.length+1, false)
    arr[0] = true
    res = []
    nums.each do |i|
        if arr[i]
            res << i
        else
            arr[i] = true
        end
    end
    res << arr.find_index(false)
    res
end
```

[726. Number of Atoms](https://leetcode.com/problems/number-of-atoms/)


## Tries

[720. Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary)
```ruby
def longest_word(words)
    words.sort!
    built = []
    ans = ""
    words.each do |str|
        if(str.length == 1 || built.include?(str[0...-1]))
            ans = str.length > ans.length ? str : ans
            built.push(str)
        end
    end
    ans
end
```

[208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)

[212. Word Search II](https://leetcode.com/problems/word-search-ii)