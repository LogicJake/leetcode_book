## 24 Game  
### 问题描述

You have 4 cards each containing a number from 1 to 9.  You need to judge whether they could operated through `*`, `/`, `+`, `-`, `(`, `)` to get the value of 24.


**Example 1:**<br />
<pre>
**Input:** [4, 1, 8, 7]
**Output:** True
**Explanation:** (8-4) * (7-1) = 24
</pre>


**Example 2:**<br />
<pre>
**Input:** [1, 2, 1, 2]
**Output:** False
</pre>


**Note:**<br>
<ol>
- The division operator `/` represents real division, not integer division.  For example, 4 / (1 - 2/3) = 12.
- Every operation done is between two numbers.  In particular, we cannot use `-` as a unary operator.  For example, with `[1, 1, 1, 1]` as input, the expression `-1 - 1 - 1 - 1` is not allowed.
- You cannot concatenate numbers together.  For example, if the input is `[1, 2, 1, 2]`, we cannot write this as 12 + 12.
</ol>

