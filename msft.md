[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = -1, rightMax = -1, water = 0;
        while(left < right){
            leftMax = Math.max(leftMax, height[left]);
            rightMax = Math.max(rightMax, height[right]);
            if(leftMax < rightMax){
                water += leftMax - height[left];
                left++;
            } else{
              water += rightMax - height[right];
                right--;
            }
        }
        
        return water;
    }
}
```
[557. Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

```java
class Solution {
    public String reverseWords(String s) {
        char[] ca = s.toCharArray();
        for(int i = 0; i < ca.length; i++){
            if(ca[i] == ' ')
                continue;
            int j = i;
            while(j + 1 < ca.length && ca[j + 1] != ' ')
                j++;
            reverse(ca, i, j);
            i = j;
        }
        return new String(ca);
    }
    private void reverse(char[] chars, int i, int j){
        int left = i, right = j;
        while(left < right){
            char c = chars[left];
            chars[left] = chars[right];
            chars[right] = c;
            left++;
            right--;
        }
    }
}
```

[445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        HashMap<Integer, Integer> m1 = new HashMap();
        HashMap<Integer, Integer> m2 = new HashMap();
        int i1 = 0, i2 = 0, carry = 0;
        ListNode head = l1;
        while(head != null){
            m1.put(i1++, head.val);
            head = head.next;
        }
        head = l2;
        while(head != null){
            m2.put(i2++, head.val);
            head = head.next;
        }
        while(i1 > 0 || i2 > 0 || carry != 0){
            int n1 = i1 > 0 ? m1.get(--i1) : 0;
            int n2 = i2 > 0 ? m2.get(--i2) : 0;
            int digit = (n1 + n2 + carry) % 10;
            carry = (n1 + n2 + carry) / 10;
            digit %= 10;
            ListNode newNode = new ListNode(digit);
            newNode.next = head;
            head = newNode;
        }
        return head;
    }
}
```

[151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
```java
class Solution {
    public String reverseWords(String s) {
        if(s == null || s.length() == 0)
            return s;
        List<String> list = new ArrayList();
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == ' ')
                continue;
            int j = i;
            while(j < s.length() && s.charAt(j) != ' ')
                j++;
            list.add(0, s.substring(i, j));
            i = j;
        }
        return String.join(" ", list);
    }
}
```

[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
```java
class Solution {
    int maxLength = 0, start = 0, end = 0;
        
    public String longestPalindrome(String s) {
        if(s == null || s.length() < 2)
            return s;
        for(int i = 0; i < s.length() - 1; i++){
            checkPalindrome(s, i, i);
            checkPalindrome(s, i, i + 1);
        }
        return s.substring(start, end + 1);
    }
    
    private void checkPalindrome(String s, int left, int right){
        while(left >= 0 && right < s.length()){
            if(s.charAt(left) != s.charAt(right))
                return;
            if(maxLength < right - left + 1){
                maxLength = right - left + 1;
                start = left;
                end = right;
            }
            left--;
            right++;
        }
    }
}
```

[54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
```java
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList();
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return res;
        
        int rowBegin = 0;
        int rowEnd = matrix.length-1;
        int colBegin = 0;
        int colEnd = matrix[0].length - 1;
        
        while (rowBegin <= rowEnd && colBegin <= colEnd) {
            // Traverse Right
            for (int j = colBegin; j <= colEnd; j ++) {
                res.add(matrix[rowBegin][j]);
            }
            rowBegin++;
            
            // Traverse Down
            for (int j = rowBegin; j <= rowEnd; j ++) {
                res.add(matrix[j][colEnd]);
            }
            colEnd--;
            
            if (rowBegin <= rowEnd) {
                // Traverse Left
                for (int j = colEnd; j >= colBegin; j --) {
                    res.add(matrix[rowEnd][j]);
                }
            }
            rowEnd--;
            
            if (colBegin <= colEnd) {
                // Traver Up
                for (int j = rowEnd; j >= rowBegin; j --) {
                    res.add(matrix[j][colBegin]);
                }
            }
            colBegin ++;
        }
        return res;
    }
}
```

[22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
```java
class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList();
        helper(ans, n, "", 0, 0);
        return ans;
    }
    
    private void helper(List<String> ans, int max, String str, int open, int close){
        if(str.length() == 2 * max){
            ans.add(str);
            return;
        }
        if(open < max)
            helper(ans, max, str + "(", open + 1, close);
        if(close < open)
            helper(ans, max, str + ")", open, close + 1);
    }
}
```

[470. Implement Rand10() Using Rand7()](https://leetcode.com/problems/implement-rand10-using-rand7/)
```java
class Solution extends SolBase {
    public int rand10() {
        int rand40 = 40;
        while (rand40 >= 40) {
            rand40 = (rand7() - 1) * 7 + rand7() - 1;
        }
        return rand40 % 10 + 1;
    }
}
```

[236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
```java
class Solution {
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null)
            return null;
        if(root == p || root == q)
            return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);

        if(left != null && right != null)
            return root;
        
        if(left != null)
            return left;
        else
            return right;
    }
    

}
```

[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

```java
class Solution {
    public int maxSubArray(int[] nums) {
        if(nums.length == 1)
            return nums[0];
        int max = nums[0];
        for(int i = 1; i < nums.length; i++){
            nums[i] = Math.max(nums[i - 1] + nums[i], nums[i]);
            if(nums[i] > max)
                max = nums[i];
        }
        return max;
    }
}
```