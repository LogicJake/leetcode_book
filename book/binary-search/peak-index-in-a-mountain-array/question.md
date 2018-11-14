## Peak Index in a Mountain Array  
### 链接  
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/  
### 问题描述
Let&#39;s call an array `A` a **mountain**&nbsp;if the following properties hold:

	- `A.length &gt;= 3`
	- There exists some `0 &lt; i&nbsp;&lt; A.length - 1` such that `A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] &gt; A[i+1] &gt; ... &gt; A[A.length - 1]`

Given an array that is definitely a mountain, return any&nbsp;`i`&nbsp;such that&nbsp;`A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] &gt; A[i+1] &gt; ... &gt; A[A.length - 1]`.

**Example 1:**

**Example 2:**

**Note:**

	1. `3 &lt;= A.length &lt;= 10000`
	1. <font face="monospace">0 &lt;= A[i] &lt;= 10^6</font>
	1. A&nbsp;is a mountain, as defined above.
