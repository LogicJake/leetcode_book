## Unique Letter String  
### 链接  
https://leetcode.com/problems/unique-letter-string/description/  
### 问题描述
A character is unique in string `S` if it occurs exactly once in it.

For example, in string `S = &quot;LETTER&quot;`, the only unique characters are `&quot;L&quot;` and `&quot;R&quot;`.

Let&#39;s define `UNIQ(S)` as the number of unique characters in string `S`.

For example, `UNIQ(&quot;LETTER&quot;) =&nbsp; 2`.

Given a string S, calculate the sum of `UNIQ(substring)` over all non-empty substrings of `S`.

If there are two or more equal substrings at different positions in `S`, we consider them different.

Since the answer can be very large, retrun the answer&nbsp;modulo&nbsp;`10 ^ 9 + 7`.

&nbsp;

**Example 1:**

**Example 2:**

&nbsp;

**Note:** `0 &lt;= S.length &lt;= 10000`.
