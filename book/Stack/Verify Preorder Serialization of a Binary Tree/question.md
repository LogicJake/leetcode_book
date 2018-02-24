## Verify Preorder Serialization of a Binary Tree  
### 链接  
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/  
### 问题描述
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as `#`.

For example, the above binary tree can be serialized to the string `"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where `#` represents a null node.


Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character `'#'` representing `null` pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as `"1,,3"`.

**Example 1:**<br>
`"9,3,4,#,#,1,#,#,2,#,6,#,#"`<br>
Return `true`

**Example 2:**<br>
`"1,#"`<br>
Return `false`

**Example 3:**<br>
`"9,#,#,1"`<br>
Return `false`

**Credits:**<br />Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.
