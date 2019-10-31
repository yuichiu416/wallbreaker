Linked lists

[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode newHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }
}
```

[328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list)
```java
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head != null) {
    
        ListNode odd = head, even = head.next, evenHead = even; 
    
        while (even != null && even.next != null) {
            odd.next = odd.next.next; 
            even.next = even.next.next; 
            odd = odd.next;
            even = even.next;
        }
        odd.next = evenHead; 
    }
    return head;
    }   
}
```

[25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group)

[146. LRU Cache](https://leetcode.com/problems/lru-cache)

Hint: This one is a bit harder. You will need to use a doubly linked list and a hash map to get O(1) time complexity for both operations.

Stacks

[682. Baseball Game](https://leetcode.com/problems/baseball-game)

[496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i)

[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

[856. Score of Parentheses](https://leetcode.com/problems/score-of-parentheses)

Queues

[225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

[232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

[189. Rotate Array](https://leetcode.com/problems/rotate-array)

Heaps

[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)

Combinatorial generation

[78. Subsets](https://leetcode.com/problems/subsets)

[46. Permutations](https://leetcode.com/problems/permutations)

[77. Combinations](https://leetcode.com/problems/combinations)

[22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses)

[89. Gray Code](https://leetcode.com/problems/gray-code)

Backtracking

[39. Combination Sum](https://leetcode.com/problems/combination-sum)

[416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)

[698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets)

[37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver)