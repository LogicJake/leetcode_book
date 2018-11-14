## Length of Longest Fibonacci Subsequence  
### 链接  
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/  
### 问题描述
A sequence `X_1, X_2, ..., X_n`&nbsp;is **fibonacci-like** if:

	- `n &gt;= 3`
	- `X_i + X_{i+1} = X_{i+2}`&nbsp;for all&nbsp;`i + 2 &lt;= n`

Given a **strictly increasing**&nbsp;array&nbsp;`A` of positive integers forming a sequence, find the **length** of the longest fibonacci-like subsequence of `A`.&nbsp; If one does not exist, return 0.

(**Recall that a subsequence is derived from another sequence `A` by&nbsp;deleting any number of&nbsp;elements (including none)&nbsp;from `A`, without changing the order of the remaining elements.&nbsp; For example, `[3, 5, 8]` is a subsequence of `[3, 4, 5, 6, 7, 8]`.**)

&nbsp;


**Example 1:**

**Example 2:**

&nbsp;

**Note:**

	- `3 &lt;= A.length &lt;= 1000`
	- `1 &lt;= A[0] &lt; A[1] &lt; ... &lt; A[A.length - 1] &lt;= 10^9`
	- **(The time limit has been reduced by 50% for submissions in Java, C, and C++.)**
