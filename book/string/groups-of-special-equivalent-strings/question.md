## Groups of Special-Equivalent Strings  
### 链接  
https://leetcode.com/problems/groups-of-special-equivalent-strings/description/  
### 问题描述
You are given an array `A` of strings.

Two strings `S` and `T` are&nbsp;**special-equivalent**&nbsp;if after any number of **moves**, S == T.

A **move** consists of choosing two indices `i` and `j` with `i % 2 == j % 2`, and swapping `S[i]` with `S[j]`.

Now, a **group of special-equivalent strings from `A`**&nbsp;is a&nbsp;non-empty subset S of `A`&nbsp;such that any string not in S&nbsp;is not special-equivalent with any string in S.

Return the number of groups of special-equivalent strings from `A`.

&nbsp;


**Example 1:**

**Example 2:**

**Example 3:**

**Example 4:**

&nbsp;

**Note:**

	- `1 &lt;= A.length &lt;= 1000`
	- `1 &lt;= A[i].length &lt;= 20`
	- All `A[i]` have the same length.
	- All `A[i]` consist of only lowercase letters.
