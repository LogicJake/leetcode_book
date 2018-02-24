## Trim a Binary Search Tree  
### 链接  
https://leetcode.com/problems/trim-a-binary-search-tree/description/  
### 问题描述

Given a binary search tree and the lowest and highest boundaries as `L` and `R`, trim the tree so that all its elements lies in `[L, R]` (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.


**Example 1:**<br />
<pre>
**Input:** 
    1
   / \
  0   2

  L = 1
  R = 2

**Output:** 
    1
      \
       2
</pre>


**Example 2:**<br />
<pre>
**Input:** 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

**Output:** 
      3
     / 
   2   
  /
 1
</pre>

