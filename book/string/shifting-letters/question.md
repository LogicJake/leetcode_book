## Shifting Letters  
### 链接  
https://leetcode.com/problems/shifting-letters/description/  
### 问题描述
We have a string `S` of lowercase letters, and an integer array `shifts`.

Call the **shift** of a letter, the next letter in the alphabet, (wrapping around so that `&#39;z&#39;` becomes `&#39;a&#39;`).&nbsp;

For example, `shift(&#39;a&#39;) = &#39;b&#39;`, `shift(&#39;t&#39;) = &#39;u&#39;`, and `shift(&#39;z&#39;) = &#39;a&#39;`.

Now for each `shifts[i] = x`, we want to shift the first `i+1`&nbsp;letters of `S`, `x` times.

Return the final string&nbsp;after all such shifts to `S` are applied.

**Example 1:**

**Note:**

	1. `1 &lt;= S.length = shifts.length &lt;= 20000`
	1. `0 &lt;= shifts[i] &lt;= 10 ^ 9`
