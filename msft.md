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
// dp approach
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

```java
// pointer approach
class Solution {
    public int maxSubArray(int[] nums) {
        if(nums == null || nums.length < 1)
            return 0;
        int currentMax = nums[0];
        int sums = 0;
        for(int i = 0; i < nums.length; i++){
            sums += nums[i];
            if(sums > currentMax)
                currentMax = sums;
            if(sums < 0)
                sums = 0;
        }
        return currentMax;
    }
}
```


[348. Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe/)
```java
public class TicTacToe {
    private int[] rows;
    private int[] cols;
    private int diagonal;
    private int antiDiagonal;

    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        rows = new int[n];
        cols = new int[n];
    }

    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    public int move(int row, int col, int player) {
        int toAdd = player == 1 ? 1 : -1;

        rows[row] += toAdd;
        cols[col] += toAdd;
        if (row == col){
            diagonal += toAdd;
        }

        if (col == (cols.length - row - 1)){
            antiDiagonal += toAdd;
        }

        int size = rows.length;
        if (Math.abs(rows[row]) == size ||
            Math.abs(cols[col]) == size ||
            Math.abs(diagonal) == size  ||
            Math.abs(antiDiagonal) == size){
            return player;
        }

        return 0;
    }
}
```

[138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
```java
class Solution {
    public Node copyRandomList(Node head) {
        if(head == null)
            return head;
        HashMap<Node, Node> map = new HashMap();
        Node ptr = head;
        while(ptr != null){
            Node clone = new Node(ptr.val);
            map.put(ptr, clone);
            ptr = ptr.next;
        }
        ptr = head;
        while(ptr != null){
            Node clone = map.get(ptr);
            clone.next = map.get(ptr.next);
            clone.random = map.get(ptr.random);
            ptr = ptr.next;
        }
        return map.get(head);
    }
}
```

[443. String Compression](https://leetcode.com/problems/string-compression/)
```java
class Solution {
    public int compress(char[] chars) {
        if (chars == null || chars.length == 0)
            return 0;
        int idx = 0, left = 0, right = 0;
        while(right < chars.length){
            char c = chars[left];
            chars[idx++] = chars[left];
            
            while(right < chars.length && c == chars[right])
                right++;
            int len = right - left;
            if(len != 1){
                for(char ch : String.valueOf(len).toCharArray())
                    chars[idx++] = ch;
            }
            left = right;
        }
        return idx;
    }
}
```

[186. Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/)

```java
class Solution {
    public void reverseWords(char[] s) {
        if(s == null || s.length == 0)
            return;
        reverse(s, 0, s.length - 1);
        for(int i = 0; i < s.length - 1; i++){
            int j = i;
            while(j + 1 < s.length && s[j + 1] != ' ')
                j++;
            reverse(s, i, j);
            i = j + 1;
        }
    }
    
    private void reverse(char[] c, int start, int end){
        while(start < end){
            char temp = c[start];
            c[start] = c[end];
            c[end] = temp;
            start++;
            end--;
        }
    }
}
```
[240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
```java
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if(matrix == null || matrix.length < 1 || matrix[0].length <1) {
            return false;
        }
        int col = matrix[0].length-1;
        int row = 0;
        while(col >= 0 && row <= matrix.length-1) {
            if(target == matrix[row][col]) {
                return true;
            } else if(target < matrix[row][col]) {
                col--;
            } else if(target > matrix[row][col]) {
                row++;
            }
        }
        return false;
    }
}
```

[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

```java
class Solution {
    public int findKthLargest(int[] nums, int k) {
        if(nums.length == 1)
            return nums[0];
        int left = 0, right = nums.length - 1;
        while(left <= right){
            int pivotPos = quickSelect(nums, left, right, k);
            int targetPos = nums.length - k;
            if(pivotPos < targetPos)
                left = pivotPos + 1;
            else if(pivotPos > targetPos)
                right = pivotPos - 1;
            else
                return nums[pivotPos];
        }
        return 0;
    }
    
    private int quickSelect(int[] nums, int left, int right, int k){
        int pivot = nums[left], pivotPos = right;
        swap(nums, left, right--);
        while(left <= right){
            if(nums[left] <= pivot)
                left++;
            else
                swap(nums, left, right--);
        }
        swap(nums, left, pivotPos);
        return left;
    }
    private void swap(int[] nums, int left, int right){
        int temp = nums[left];
        nums[left] = nums[right];
        nums[right] = temp;
    }
}
```

[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
```java
public class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    public boolean isValidBST(TreeNode root, long minVal, long maxVal) {
        if (root == null) 
            return true;
        if (root.val >= maxVal || root.val <= minVal)
            return false;
        return isValidBST(root.left, minVal, root.val) && isValidBST(root.right, root.val, maxVal);
    }
}
```

[73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
```java
class Solution {
    public void setZeroes(int[][] matrix) {
        boolean fr = false,fc = false;
        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < matrix[0].length; j++) {
                if(matrix[i][j] == 0) {
                    if(i == 0) fr = true;
                    if(j == 0) fc = true;
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        for(int i = 1; i < matrix.length; i++) {
            for(int j = 1; j < matrix[0].length; j++) {
                if(matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        if(fr) {
            for(int j = 0; j < matrix[0].length; j++) {
                matrix[0][j] = 0;
            }
        }
        if(fc) {
            for(int i = 0; i < matrix.length; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
```

[1. Two Sum](https://leetcode.com/problems/two-sum/)

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, int[]> map = new HashMap();
        
        for(int i = 0; i < nums.length; i++){
            int[] pair = new int[2];
            if(map.containsKey(nums[i])){
                map.get(nums[i])[1] = i;
                return map.get(nums[i]);
            }
            else{
                pair[0] = i;
                map.put(target - nums[i], pair);
            }
        }
        return null;
    }
}
```