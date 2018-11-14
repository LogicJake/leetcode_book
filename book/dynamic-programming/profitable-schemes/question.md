## Profitable Schemes  
### 链接  
https://leetcode.com/problems/profitable-schemes/description/  
### 问题描述
There are G people in a gang, and a list of various crimes they could commit.

The `i`-th crime generates a `profit[i]` and requires `group[i]` gang members to participate.

If a gang member participates in one crime, that member can&#39;t participate in another crime.

Let&#39;s call a **profitable&nbsp;scheme**&nbsp;any subset of these crimes that generates at least `P` profit, and the total number of gang members participating in that subset of crimes is at most G.

How many schemes can be chosen?&nbsp; Since the answer may be very&nbsp;large, **return it modulo** `10^9 + 7`.

&nbsp;

**Example 1:**

**Example 2:**

&nbsp;

**Note:**

	1. `1 &lt;= G &lt;= 100`
	1. `0 &lt;= P &lt;= 100`
	1. `1 &lt;= group[i] &lt;= 100`
	1. `0 &lt;= profit[i] &lt;= 100`
	1. `1 &lt;= group.length = profit.length &lt;= 100`
