## Kth Smallest Number in Multiplication Table  
### 链接  
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/description/  
### 问题描述

Nearly every one have used the [Multiplication Table](https://en.wikipedia.org/wiki/Multiplication_table). But could you find out the `k-th` smallest number quickly from the multiplication table?



Given the height `m` and the length `n` of a `m * n` Multiplication Table, and a positive integer `k`, you need to return the `k-th` smallest number in this table.


**Example 1:**<br />
<pre>
**Input:** m = 3, n = 3, k = 5
**Output:** 
**Explanation:** 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
</pre>


**Example 2:**<br />
<pre>
**Input:** m = 2, n = 3, k = 6
**Output:** 
**Explanation:** 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
</pre>


**Note:**<br>
<ol>
- The `m` and `n` will be in the range [1, 30000].
- The `k` will be in the range [1, m * n]
</ol>

