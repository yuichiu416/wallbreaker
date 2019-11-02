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
```java
class LRUCache {
    class Node{
        int key;
        int value;
        Node prev;
        Node next;
    }
    
    private int count;
    private int capacity;
    private Node head, tail;
    private HashMap<Integer, Node> cache = new HashMap<Integer, Node>();
    

    public LRUCache(int capacity) {
        this.count = 0;
        this.capacity = capacity;
        head = new Node();
        tail = new Node();
        head.prev = null;
        head.next = tail;
        tail.prev = head;
        tail.next = null;
    }
    
    public int get(int key) {
        Node node = cache.get(key);
        if(node == null)
            return -1;
        this.moveToHead(node);
        return node.value;
    }
    
    public void put(int key, int value) {
        Node node = cache.get(key);
        if(node == null){
            Node newNode = new Node();
            newNode.key = key;
            newNode.value = value;
            this.cache.put(key, newNode);
            this.addNode(newNode);
            
            count++;
            if(count > capacity){
                Node tail = this.popTail();
                this.cache.remove(tail.key);
                count--;
            }
        } else{
            node.value = value;
            this.moveToHead(node);
        }
    }
    
    private void addNode(Node node){
        node.prev = head;
        node.next = head.next;
        
        head.next.prev = node;
        head.next = node;
    }
    
    private void removeNode(Node node){
        Node prev = node.prev;
        Node next = node.next;
        
        prev.next = next;
        next.prev = prev;
    }
    
    private void moveToHead(Node node){
        this.removeNode(node);
        this.addNode(node);
    }
    
    private Node popTail(){
        Node t = tail.prev;
        this.removeNode(t);
        return t;
    }
    
    
}

```

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