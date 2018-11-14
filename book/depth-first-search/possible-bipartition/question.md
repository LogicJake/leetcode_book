## Possible Bipartition  
### 链接  
https://leetcode.com/problems/possible-bipartition/description/  
### 问题描述
Given a set of `N`&nbsp;people (numbered `1, 2, ..., N`), we would like to split everyone into two groups of **any** size.

Each person may dislike some other people, and they should not go into the same group.&nbsp;

Formally, if `dislikes[i] = [a, b]`, it means it is not allowed to put the people numbered `a` and `b` into the same group.

Return `true`&nbsp;if and only if it is possible to split everyone into two groups in this way.

&nbsp;


**Example 1:**

**Example 2:**

**Example 3:**

&nbsp;

**Note:**

	1. `1 &lt;= N &lt;= 2000`
	1. `0 &lt;= dislikes.length &lt;= 10000`
	1. `1 &lt;= dislikes[i][j] &lt;= N`
	1. `dislikes[i][0] &lt; dislikes[i][1]`
	1. There does not exist `i != j` for which `dislikes[i] == dislikes[j]`.
