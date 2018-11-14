## Construct String from Binary Tree  
### 链接  
https://leetcode.com/problems/construct-string-from-binary-tree/description/  
### 问题描述
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

**Example 1:**<br />
<pre>
**Input:** Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

**Output:** "1(2(4))(3)"
<br/>**Explanation:** Originallay it needs to be "1(2(4)())(3()())", <br/>but you need to omit all the unnecessary empty parenthesis pairs. <br/>And it will be "1(2(4))(3)".
</pre>


**Example 2:**<br />
<pre>
**Input:** Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

**Output:** "1(2()(4))(3)"
<br/>**Explanation:** Almost the same as the first example, <br/>except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
</pre>

