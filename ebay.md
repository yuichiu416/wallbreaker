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