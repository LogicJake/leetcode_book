## Random Flip Matrix  
### 链接  
https://leetcode.com/problems/random-flip-matrix/description/  
### 问题描述
You are given the number of rows `n_rows`&nbsp;and number of columns `n_cols`&nbsp;of a&nbsp;2D&nbsp;binary matrix&nbsp;where all values are initially 0.&nbsp;Write a function `flip`&nbsp;which chooses&nbsp;a 0 value&nbsp;[uniformly at random](https://en.wikipedia.org/wiki/Discrete_uniform_distribution),&nbsp;changes it to 1,&nbsp;and then returns the position `[row.id, col.id]` of that value. Also, write a function `reset` which sets all values back to 0.&nbsp;**Try to minimize the number of calls to system&#39;s Math.random()** and optimize the time and&nbsp;space complexity.

Note:

	1. `1 &lt;= n_rows, n_cols&nbsp;&lt;= 10000`
	1. `0 &lt;= row.id &lt; n_rows` and `0 &lt;= col.id &lt; n_cols`
	1. `flip`&nbsp;will not be called when the matrix has no&nbsp;0 values left.
	1. the total number of calls to&nbsp;`flip`&nbsp;and `reset`&nbsp;will not exceed&nbsp;1000.

**Example 1:**

**Example 2:**

**Explanation of Input Syntax:**

The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments. `Solution`&#39;s constructor&nbsp;has two arguments, `n_rows` and `n_cols`.&nbsp;`flip`&nbsp;and `reset` have&nbsp;no&nbsp;arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren&#39;t any.
