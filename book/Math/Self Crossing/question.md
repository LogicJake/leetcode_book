## Self Crossing  
### 问题描述

    You are given an array *x* of `n` positive numbers. You start at point `(0,0)` and moves `x[0]` metres to the north, then `x[1]` metres to the west,
    `x[2]` metres to the south,
    `x[3]` metres to the east and so on. In other words, after each move your direction changes
    counter-clockwise.



    Write a one-pass algorithm with `O(1)` extra space to determine, if your path crosses itself, or not.



**Example 1:**<br/>
<pre>
Given *x* = `[2, 1, 1, 2]`,
?????
?   ?
???????>
    ?

Return **true** (self crossing)
</pre>



**Example 2:**<br/>
<pre>
Given *x* = `[1, 2, 3, 4]`,
????????
?      ?
?
?
?????????????>

Return **false** (not self crossing)
</pre>



**Example 3:**<br/>
<pre>
Given *x* = `[1, 1, 1, 1]`,
?????
?   ?
?????>

Return **true** (self crossing)
</pre>


**Credits:**<br />Special thanks to [@dietpepsi](https://leetcode.com/discuss/user/dietpepsi) for adding this problem and creating all test cases.
