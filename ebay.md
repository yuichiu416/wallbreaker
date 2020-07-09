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

[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

```ruby
def letter_combinations(digits)
    map = {}
    map["2"] = "abc"
    map["3"] = "def"
    map["4"] = "ghi"
    map["5"] = "jkl"
    map["6"] = "mno"
    map["7"] = "pqrs"
    map["8"] = "tuv"
    map["9"] = "wxyz"
    ans = []
    queue = [""]
    for i in 0...digits.length
        while queue[0].length == i
            base = queue.shift()
            map[digits[i]].each_char do |c|
                str = base + c
                queue << str
                ans << str if str.length == digits.length
            end
        end
    end
    ans
end
```
[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

```ruby
def is_valid(s)
    stack = []
    left = "([{"
    right = ")]}"
    s.each_char do |c|
        if left.include?(c)
            stack << c
        elsif right.include?(c)
            return false if stack.empty?
            last = stack[-1]
            index = left.index(last)
            if right[index] != c
                return false
            else
                stack.pop()
            end
        end
    end
    stack.empty?           
end
```
[](https://leetcode.com/problems/generate-parentheses/)

```ruby
def generate_parenthesis(n)
    ans = []
    helper(n, "", 0, 0, ans)
    ans
end

def helper(max, currentStr, left, right, ans)
    if left + right == max * 2
        ans << currentStr
        return
    end
    return if left > max
    
    if left < max
        helper(max, currentStr + "(", left + 1, right, ans)
    end
    if right < left
        helper(max, currentStr + ")", left, right + 1, ans)
    end
    
end
```
[28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)

```ruby
def str_str(haystack, needle)
    return 0 if needle == ""
    i = 0
    j = needle.length
    while true
        if haystack[i...i + needle.length] == needle
            return i
        elsif j >= haystack.length
            return -1
        end
        i += 1
        j += 1
    end
    -1
end
```

[6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

```ruby
def convert(s, num_rows)
    ans = ""
    i = 0
    rows = Array.new(num_rows, "")
    while i < s.length
        row = 0
        while row < num_rows && i < s.length
            rows[row] += s[i]
            i += 1
            row += 1
        end
        row = num_rows - 2
        while row >= 1 && i < s.length
            rows[row] += s[i]
            i += 1
            row -= 1
        end
        row += 2
    end
    rows.each do |r|
        ans += r
    end
    ans
end
```

[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
```ruby
def group_anagrams(strs)
    maps = {}
    strs.each do |str|
        sorted = str.split("").sort.join("")
        maps[sorted] = [] if !maps[sorted]
        maps[sorted] << str
    end
    maps.values
end
```

[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
```ruby
def top_k_frequent(nums, k)
    map = Hash.new(0)
    max = 0
    nums.each do |n|
        map[n] += 1
        if map[n] > max
            max = map[n]
        end
    end
    count = Array.new(nums.length + 1) {Array.new}
    map.each do |k, v|
        count[v] << k
    end
    i = count.length - 1
    ans = []
    while ans.length < k
        while !count[i].empty? && ans.length < k
            ans << count[i].pop
        end
        i -= 1
    end
    ans
end
```


[1. Two Sum](https://leetcode.com/problems/two-sum/)
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        Map<Integer, Integer> map = new HashMap();
        for(int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) != null) {
                ans[0] = map.get(nums[i]);
                ans[1] = i;
                return ans;
            } else {
                map.put(target - nums[i], i);
            }
        }
        return null;
    }
}
```

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0, right = 0;
        int max = 0;
        Map<Character, Integer> map = new HashMap();

        while (left <= right && right < s.length()) {
            char c = s.charAt(right);
            if (map.get(c) != null) {
                left = Math.max(map.get(c) + 1, left);
            }
            map.put(c, right);
        
            max = Math.max(right - left + 1, max);
            right++;
        }
        return max;
    }
}
```
[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

```java
class Solution {
    public int maxArea(int[] height) {
        if (height == null || height.length < 2) {
            return 0;
        }
        int left = 0, right = height.length - 1;
        int leftMax = height[left], rightMax = height[right];
        int max = (right - left) * Math.min(leftMax, rightMax);
        while (left < right) {
            max = Math.max(max, (right - left) * Math.min(leftMax, rightMax));
            if (leftMax < rightMax) {
                left++;
                leftMax = Math.max(height[left], leftMax);
            } else {
                right--;
                rightMax = Math.max(height[right], rightMax);
            }
        }
        return max;
    }
}
```
[39. Combination Sum](https://leetcode.com/problems/combination-sum/)
```java
class Solution {
    List<List<Integer>> ans = new ArrayList();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        helper(candidates, target, new ArrayList<Integer>(), 0);
        return ans;
    }
    private void helper(int[] candidates, int target, List<Integer> set, int start) {
        if (target == 0) {
            ans.add(new ArrayList(set));
            return;
        }
        for(int i = start; i < candidates.length; i++) {
            int newTarget = target - candidates[i];
            if (newTarget >= 0) {
                set.add(candidates[i]);
                helper(candidates, newTarget, set, i);
                set.remove(set.size() - 1);
            }
        }
    }
}
```

[78. Subsets](https://leetcode.com/problems/subsets/)

```java
class Solution {
    List<List<Integer>> ans = new ArrayList();
    public List<List<Integer>> subsets(int[] nums) {
        helper(nums, new ArrayList<Integer>(), 0);
        return ans;
    }
    
    private void helper(int[] nums, List<Integer> current, int start) {
        ans.add(new ArrayList(current));
        for(int i = start; i < nums.length; i++) {
            current.add(nums[i]);
            helper(nums, current, i + 1);
            current.remove(current.size() - 1);
        }
    }
}
```
[90. Subsets II](https://leetcode.com/problems/subsets-ii/)

```java
class Solution {
    List<List<Integer>> ans = new ArrayList();
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        helper(nums, new ArrayList<Integer>(), 0);
        return ans;
    }
    private void helper(int[] nums, List<Integer> current, int start) {
        ans.add(new ArrayList(current));
        for(int i = start; i < nums.length; i++){
            if(i > start && nums[i] == nums[i - 1]) {
                continue;
            }
            current.add(nums[i]);
            helper(nums, current, i + 1);
            current.remove(current.size() - 1);
        }
    }
}
```

[46. Permutations](https://leetcode.com/problems/permutations/)

```java
class Solution {
    List<List<Integer>> ans = new ArrayList();
    public List<List<Integer>> permute(int[] nums) {
        helper(nums, new ArrayList<Integer>(), 0);
        return ans;
    }
    private void helper(int[] nums, List<Integer> current, int start) {
        if (current.size() == nums.length) {
            ans.add(new ArrayList(current));
            return;
        }
        
        for(int i = 0; i < nums.length; i++) {
            if (current.contains(nums[i])){
                continue;
            }
            current.add(nums[i]);
            helper(nums, current, start + 1);
            current.remove(current.size() - 1);
        }
    }
}
```

[47. Permutations II](https://leetcode.com/problems/permutations-ii/)
```java
class Solution {
    List<List<Integer>> ans = new ArrayList();
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        helper(nums, new ArrayList<Integer>(), new boolean[nums.length]);
        return ans;
    }
    private void helper(int[] nums, List<Integer> current, boolean[] used) {
        if (current.size() == nums.length) {
            ans.add(new ArrayList(current));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (used[i] || i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) {
                continue;
            }
            used[i] = true;
            current.add(nums[i]);
            helper(nums, current, used);
            used[i] = false;
            current.remove(current.size() - 1);
        }
    }
}
```

[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

```java
class Solution {
    String longest = "";
    public String longestPalindrome(String s) {
        for(int i = 0; i < s.length(); i++) {
            helper(s, i, i);
            helper(s, i, i + 1);
        }
        return longest;
    }
    private void helper(String s, int left, int right) {
        while (left >= 0 && right < s.length()) {
            if (s.charAt(left) != s.charAt(right)) {
                break;
            }
            left--;
            right++;
        }
        left++;
        right--;
        if (right - left + 1 > longest.length()) {
            longest = s.substring(left, right + 1);
        }
    }
}
```

[905. Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)

```java
class Solution {
    public int[] sortArrayByParity(int[] A) {
        if (A == null || A.length < 2) {
            return A;        
        }
        int left = 0, right = A.length - 1;
        while (left < right) {
            while(left < right && A[left] % 2 == 0) {
                left++;
            }
            while(left < right && A[right] % 2 == 1) {
                right--;
            }
            if (left >= right) {
                break;
            }
            swap(A, left, right);
            left++;
            right--;
        }
        return A;
    }
    private void swap(int[] A, int l, int r) {
        int temp = A[l];
        A[l] = A[r];
        A[r] = temp;
    }
}
```

[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
```java
class Solution {
    public boolean isValid(String s) {
        List<Character> stack = new ArrayList();
        String leftStr = "([{";
        String rightStr = "}])";
        if (s.length() % 2 != 0) {
            return false;
        }
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (leftStr.indexOf(c) != -1) {
                stack.add(c);
            } else {
                if (stack.size() == 0) {
                    return false;
                }
                char match = stack.remove(stack.size() - 1);
                if (match == '(' && c == ')') {
                    continue;
                } else if (match == '[' && c == ']') {
                    continue;
                } else if(match == '{' && c == '}') {
                    continue;
                } else {
                    return false;
                }
            }
        }
        return stack.size() == 0;
        
    }
}
```

[131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

```java
class Solution {
    List<List<String>> ans = new ArrayList();
    public List<List<String>> partition(String s) {
        helper(s, new ArrayList<String>(), 0);
        return ans;
    }
    private void helper(String s, List<String> tempList, int start) {
        if (start == s.length()) {
            ans.add(new ArrayList(tempList));
            return;
        }
        for (int i = start; i < s.length(); i++) {
            String sub = s.substring(start, i + 1);
            if (isPalindrome(sub)) {
                tempList.add(sub);
                helper(s, tempList, i + 1);
                tempList.remove(tempList.size() - 1);
            }
        }
    }
    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
}
```