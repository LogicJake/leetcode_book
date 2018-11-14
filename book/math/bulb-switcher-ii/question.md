## Bulb Switcher II  
### 链接  
https://leetcode.com/problems/bulb-switcher-ii/description/  
### 问题描述

There is a room with `n` lights which are turned on initially and 4 buttons on the wall. After performing exactly `m` unknown operations towards buttons, you need to return how many different kinds of status of the `n` lights could be.



Suppose `n` lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

<ol>
- Flip all the lights.
- Flip lights with even numbers.
- Flip lights with odd numbers.
- Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...
</ol>


**Example 1:**<br />
<pre>
**Input:** n = 1, m = 1.
**Output:** 2
**Explanation:** Status can be: [on], [off]
</pre>


**Example 2:**<br />
<pre>
**Input:** n = 2, m = 1.
**Output:** 3
**Explanation:** Status can be: [on, off], [off, on], [off, off]
</pre>


**Example 3:**<br />
<pre>
**Input:** n = 3, m = 1.
**Output:** 4
**Explanation:** Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
</pre>


**Note:**
`n` and `m` both fit in range [0, 1000].

