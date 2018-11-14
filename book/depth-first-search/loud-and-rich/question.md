## Loud and Rich  
### 链接  
https://leetcode.com/problems/loud-and-rich/description/  
### 问题描述
In a group of N people (labelled `0, 1, 2, ..., N-1`), each person has different amounts of money, and different levels of quietness.

For convenience, we&#39;ll call the person with label `x`, simply &quot;person `x`&quot;.

We&#39;ll say that `richer[i] = [x, y]` if person `x`&nbsp;definitely has more money than person&nbsp;`y`.&nbsp; Note that `richer`&nbsp;may only be a subset of valid observations.

Also, we&#39;ll say `quiet[x] = q` if person <font face="monospace">x</font>&nbsp;has quietness `q`.

Now, return `answer`, where `answer[x] = y` if `y` is the least quiet person (that is, the person `y` with the smallest value of `quiet[y]`), among all people&nbsp;who definitely have&nbsp;equal to or more money than person `x`.

&nbsp;

**Example 1:**

**Note:**

	1. `1 &lt;= quiet.length = N &lt;= 500`
	1. `0 &lt;= quiet[i] &lt; N`, all `quiet[i]` are different.
	1. `0 &lt;= richer.length &lt;= N * (N-1) / 2`
	1. `0 &lt;= richer[i][j] &lt; N`
	1. `richer[i][0] != richer[i][1]`
	1. `richer[i]`&#39;s are all different.
	1. The&nbsp;observations in `richer` are all logically consistent.
