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
