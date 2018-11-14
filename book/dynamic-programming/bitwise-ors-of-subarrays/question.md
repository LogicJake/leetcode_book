## Bitwise ORs of Subarrays  
### 链接  
https://leetcode.com/problems/bitwise-ors-of-subarrays/description/  
### 问题描述
We have an array `A` of non-negative integers.

For every (contiguous) subarray `B =&nbsp;[A[i], A[i+1], ..., A[j]]` (with `i &lt;= j`), we take the bitwise OR of all the elements in `B`, obtaining a result <font face="monospace">`A[i] | A[i+1] | ... | A[j]`.</font>

Return the number of possible&nbsp;results.&nbsp; (Results that occur more than once are only counted once in the final answer.)

&nbsp;

**Example 1:**

**Example 2:**

**Example 3:**

&nbsp;

**Note:**

	1. `1 &lt;= A.length &lt;= 50000`
	1. `0 &lt;= A[i] &lt;= 10^9`
