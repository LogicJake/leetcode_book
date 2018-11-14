## Valid Permutations for DI Sequence  
### 链接  
https://leetcode.com/problems/valid-permutations-for-di-sequence/description/  
### 问题描述
We are given `S`, a length `n` string of characters from the set `{&#39;D&#39;, &#39;I&#39;}`. (These letters stand for &quot;decreasing&quot; and &quot;increasing&quot;.)

A&nbsp;**valid permutation**&nbsp;is a permutation `P[0], P[1], ..., P[n]` of integers&nbsp;`{0, 1, ..., n}`, such that for all `i`:

	- If `S[i] == &#39;D&#39;`, then `P[i] &gt; P[i+1]`, and;
	- If `S[i] == &#39;I&#39;`, then `P[i] &lt; P[i+1]`.

How many valid permutations are there?&nbsp; Since the answer may be large, **return your answer modulo `10^9 + 7`**.

&nbsp;

**Example 1:**

&nbsp;

**Note:**

	1. `1 &lt;= S.length &lt;= 200`
	1. `S` consists only of characters from the set `{&#39;D&#39;, &#39;I&#39;}`.

&nbsp;
