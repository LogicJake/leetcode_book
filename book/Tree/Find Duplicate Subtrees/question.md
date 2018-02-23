## Find Duplicate Subtrees  
### 问题描述

Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any **one** of them. 


Two trees are duplicate if they have the same structure with same node values.


**Example 1: **<br>
<pre>
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
</pre>
The following are two duplicate subtrees:
<pre>
      2
     /
    4
</pre>
and
<pre>
    4
</pre>
Therefore, you need to return above trees' root in the form of a list.

