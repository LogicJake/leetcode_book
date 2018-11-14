## Verify Preorder Serialization of a Binary Tree  
### 链接  
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/  
### 问题描述
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node&#39;s value. If it is a null node, we record using a sentinel value such as `#`.

```
&quot;9,3,4,#,#,1,#,#,2,#,6,#,#&quot;</code>
**Output: **<code>true
```

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as `&quot;1,,3&quot;`.

**Example 2:**

```
&quot;1,#&quot;</code>
**Output: **`false`
</pre>

**Example 3:**

<pre>
**Input: **`&quot;9,#,#,1&quot;`
**Output: **<code>false
```
