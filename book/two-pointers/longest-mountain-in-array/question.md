## Longest Mountain in Array  
### 链接  
https://leetcode.com/problems/longest-mountain-in-array/description/  
### 问题描述
Let&#39;s call any (contiguous) subarray B (of A)&nbsp;a **mountain** if the following properties hold:

	- `B.length &gt;= 3`
	- There exists some `0 &lt; i&nbsp;&lt; B.length - 1` such that `B[0] &lt; B[1] &lt; ... B[i-1] &lt; B[i] &gt; B[i+1] &gt; ... &gt; B[B.length - 1]`

(Note that B could be any subarray of A, including the entire array A.)

Given an array `A`&nbsp;of integers,&nbsp;return the length of the longest&nbsp;**mountain**.&nbsp;

Return `0` if there is no mountain.

&nbsp;

**Example 1:**

**Example 2:**

&nbsp;

**Note:**

	1. `0 &lt;= A.length &lt;= 10000`
	1. `0 &lt;= A[i] &lt;= 10000`
