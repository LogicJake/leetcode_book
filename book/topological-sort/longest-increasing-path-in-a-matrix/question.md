## Longest Increasing Path in a Matrix  
### 链接  
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/  
### 问题描述
Given an integer matrix, find the length of the longest increasing path.


From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).


**Example 1:**
<pre>
nums = [
  [<font color="red">9</font>,9,4],
  [<font color="red">6</font>,6,8],
  [<font color="red">2</font>,<font color="red">1</font>,1]
]
</pre>



Return `4`<br/>

The longest increasing path is `[1, 2, 6, 9]`.


**Example 2:**
<pre>
nums = [
  [<font color="red">3</font>,<font color="red">4</font>,<font color="red">5</font>],
  [3,2,<font color="red">6</font>],
  [2,2,1]
]
</pre>



Return `4`<br/>

The longest increasing path is `[3, 4, 5, 6]`. Moving diagonally is not allowed.

**Credits:**<br />Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.
