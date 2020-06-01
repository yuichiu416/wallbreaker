[643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)
```ruby
def find_max_average(nums, k)
    maxSum = 0
    for i in 0...k
        maxSum += nums[i]
    end
    sum = maxSum
    (k...nums.length).each do |i|
        sum = sum + nums[i] - nums[i - k]
        maxSum = [sum, maxSum].max
    end
    maxSum / 1.0 / k
end
```

[268. Missing Number](https://leetcode.com/problems/missing-number/)
```ruby
def missing_number(nums)
    xor = 0
    i = 0
    (0...nums.length).each do |i|
        xor = xor ^ i ^ nums[i]
    end
    xor ^ nums.length
end
```

[139. Word Break](https://leetcode.com/problems/word-break/)
```ruby
def word_break(s, word_dict)
    return false if !s || !word_dict
    dp = Array.new(s.length, false)
    for right in 0...s.length
        for left in 0..right
            if word_dict.include?(s[left..right]) && (dp[left - 1] || left == 0)
                dp[right] = true
            end
        end
    end
    dp[-1]
end
```

[94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
```ruby
def inorder_traversal(root)
    return [] if root.nil?
    ans = []
    ans += inorder_traversal(root.left)
    ans << root.val
    ans += inorder_traversal(root.right)
    ans
end
```

[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
```ruby
def is_valid_bst(root)
    helper(root, Float::INFINITY, -Float::INFINITY)
end

def helper(root, max_val, min_val)
    return true if root.nil?
    if root.val <= min_val || root.val >=max_val
        return false
    else
        return helper(root.left, root.val, min_val) && helper(root.right, max_val, root.val)
    end
end
```

[227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
```ruby
def calculate(s)
    stack = []
    num = 0
    operators = "+-*/"
    currentOperator = "+"
    s.each_char.with_index do |c, i|
        if /\d/.match(c)
            num = num * 10 + c.to_i
        end
        if operators.include?(c) || i == s.length - 1
            if currentOperator == "+"
                stack.push(num)
            elsif currentOperator == "-"
                stack.push(-num)
            elsif currentOperator == "*"
                stack.push(stack.pop() * num)
            elsif currentOperator == "/"
                stack.push((stack.pop().to_f / num).truncate)
            end
            currentOperator = c
            num = 0
        end
    end
    sum = 0
    stack.each{ |num| sum += num}
    sum
end
```

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
```ruby
def length_of_longest_substring(s)
    map = {}
    max = 0
    left, right = 0, 0
    while left <= right && right < s.length
        c = s[right]
        if map[c]
            left = [map[c] + 1, left].max
        end
        map[c] = right
        max = [right - left + 1, max].max
        right += 1
    end
    max
end
```

[](https://leetcode.com/problems/3sum/)

```ruby
def three_sum(nums)
    nums.sort!
    ans = []
    for i in 0...nums.length - 1
        remaining = 0 - nums[i]
        left = i + 1
        right = nums.length - 1
        if i == 0 || nums[i] != nums[i - 1]
            while left < right
                if nums[left] + nums[right] > remaining
                    right -= 1
                elsif nums[left] + nums[right] < remaining
                    left += 1
                else
                    ans << [nums[i], nums[left], nums[right]]
                    while left < right && nums[left] == nums[left + 1]
                        left += 1
                    end
                    while left < right && nums[right] == nums[right - 1]
                        right -= 1
                    end
                    left += 1
                    right -= 1
                end
            end
        end
    end
    ans
end
```

[16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

```ruby
def three_sum_closest(nums, target)
    nums.sort!
    ans = Float::INFINITY
    
    for i in 0...nums.length - 1
        left = i + 1
        right = nums.length - 1
        while left < right
            sum = nums[i] + nums[left] + nums[right]
            if sum > target
                right -= 1
            elsif sum < target
                left += 1
            else
                return target
            end
            ans = sum if (sum - target).abs < (ans - target).abs
        end
    end
    ans
end
```

[26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
```ruby
def remove_duplicates(nums)
    i = 1
    while i < nums.length
        if nums[i] == nums[i - 1]
            nums.delete_at(i)
            next
        end
        i += 1
    end
end
```

[27. Remove Element](https://leetcode.com/problems/remove-element/)

```ruby
def remove_element(nums, val)
    i = 0
    while i < nums.length
        if nums[i] == val
            nums.delete_at(i) 
            next
        end
        i += 1
    end
end
```

[31. Next Permutation](https://leetcode.com/problems/next-permutation/)

```ruby
def next_permutation(nums)
    i = nums.length - 2
    while i >= 0 && nums[i] >= nums[i + 1]
        i -= 1 # find the first non-decending pivot
    end
    if i >= 0
        j = nums.length - 1
        while nums[j] <= nums[i]
            j -= 1
        end
        nums[i], nums[j] = nums[j], nums[i]
    end
    reverse(nums, i + 1, nums.length - 1)
end

def reverse(nums, i, j)
    while i < j
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    end
end
```