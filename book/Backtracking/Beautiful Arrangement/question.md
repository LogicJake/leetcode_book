## Beautiful Arrangement  
### 问题描述

Suppose you have **N** integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these **N** numbers successfully if one of the following is true for the i<sub>th</sub> position (1 <= i <= N) in this array:
<ol>
- The number at the i<sub>th</sub> position is divisible by **i**.
- **i** is divisible by the number at the i<sub>th</sub> position.
</ol>



Now given N, how many beautiful arrangements can you construct?


**Example 1:**<br />
<pre>
**Input:** 2
**Output:** 2
**Explanation:** 
<br/>The first beautiful arrangement is [1, 2]:
<br/>Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
<br/>Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
<br/>The second beautiful arrangement is [2, 1]:
<br/>Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
<br/>Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
</pre>


**Note:**<br>
<ol>
- **N** is a positive integer and will not exceed 15.
</ol>

