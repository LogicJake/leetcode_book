## Continuous Subarray Sum  
### 链接  
https://leetcode.com/problems/continuous-subarray-sum/description/  
### 问题描述

Given a list of **non-negative** numbers and a target **integer** k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of **k**, that is, sums up to n*k where n is also an **integer**.


**Example 1:**<br />
<pre>
**Input:** [23, 2, 4, 6, 7],  k=6
**Output:** True
**Explanation:** Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
</pre>


**Example 2:**<br />
<pre>
**Input:** [23, 2, 6, 4, 7],  k=6
**Output:** True
**Explanation:** Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
</pre>


**Note:**<br>
<ol>
- The length of the array won't exceed 10,000.
- You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
</ol>

