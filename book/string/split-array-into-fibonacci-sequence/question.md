## Split Array into Fibonacci Sequence  
### 链接  
https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/  
### 问题描述
Given a string `S`&nbsp;of digits, such as `S = &quot;123456579&quot;`, we can split it into a **Fibonacci-like sequence**&nbsp;`[123, 456, 579].`

Formally, a Fibonacci-like sequence is a list&nbsp;`F` of non-negative integers such that:

	- `0 &lt;= F[i] &lt;= 2^31 - 1`, (that is,&nbsp;each integer fits a 32-bit signed integer type);
	- `F.length &gt;= 3`;
	- and` F[i] + F[i+1] = F[i+2] `for all `0 &lt;= i &lt; F.length - 2`.

Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from `S`, or return `[]` if it cannot be done.

**Example 1:**

**Example 2:**

**Example 3:**

**Example 4:**

**Example 5:**

**Note: **

	1. `1 &lt;= S.length&nbsp;&lt;= 200`
	1. `S` contains only digits.
