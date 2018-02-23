## Largest Divisible Subset  
### 问题描述

Given a set of **distinct** positive integers, find the largest subset such that every pair (S<sub>i</sub>, S<sub>j</sub>) of elements in this subset satisfies: S<sub>i</sub> % S<sub>j</sub> = 0 or S<sub>j</sub> % S<sub>i</sub> = 0.


If there are multiple solutions, return any subset is fine.


**Example 1:**
<pre>
nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
</pre>


**Example 2:**
<pre>
nums: [1,2,4,8]

Result: [1,2,4,8]
</pre>


**Credits:**<br />Special thanks to [@Stomach_ache](https://leetcode.com/stomach_ache) for adding this problem and creating all test cases.
