## Random Pick with Blacklist  
### 链接  
https://leetcode.com/problems/random-pick-with-blacklist/description/  
### 问题描述
Given a blacklist&nbsp;`B` containing unique integers&nbsp;from `[0, N)`, write a function to return a uniform random integer from `[0, N)` which is **NOT**&nbsp;in `B`.

Optimize it such that it minimizes the call to system&rsquo;s `Math.random()`.

**Note:**

	1. `1 &lt;= N &lt;= 1000000000`
	1. `0 &lt;= B.length &lt; min(100000, N)`
	1. `[0, N)`&nbsp;does NOT include N. See [interval notation](https://en.wikipedia.org/wiki/Interval_(mathematics)).

**Example 1:**

**Example 2:**

**Example 3:**

**Example 4:**

**Explanation of Input Syntax:**

The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments.&nbsp;`Solution`&#39;s&nbsp;constructor has two arguments,&nbsp;`N` and the blacklist `B`. `pick` has no arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren&#39;t any.
