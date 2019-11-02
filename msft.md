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