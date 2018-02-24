## Validate Binary Search Tree  
### 链接  
https://leetcode.com/problems/validate-binary-search-tree/description/  
### 问题描述

Given a binary tree, determine if it is a valid binary search tree (BST).



Assume a BST is defined as follows:
<ul>
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.
</ul>


**Example 1:**<br />
<pre>
    2
   / \
  1   3
</pre>
Binary tree `[2,1,3]`, return true.


**Example 2:**<br />
<pre>
    1
   / \
  2   3
</pre>
Binary tree `[1,2,3]`, return false.

