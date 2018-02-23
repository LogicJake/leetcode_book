## Populating Next Right Pointers in Each Node  
### 问题描述

Given a binary tree
<pre>
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
</pre>


Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.


**Note:**
<ul>
- You may only use constant extra space.
- You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
</ul>



For example,<br />
Given the following perfect binary tree,<br />
<pre>
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
</pre>



After calling your function, the tree should look like:<br />
<pre>
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
</pre>

