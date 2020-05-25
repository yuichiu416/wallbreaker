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