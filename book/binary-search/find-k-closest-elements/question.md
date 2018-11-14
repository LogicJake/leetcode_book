## Find K Closest Elements  
### 链接  
https://leetcode.com/problems/find-k-closest-elements/description/  
### 问题描述

Given a sorted array, two integers `k` and `x`, find the `k` closest elements to `x` in the array.  The result should also be sorted in ascending order.
If there is a tie,  the smaller elements are always preferred.


**Example 1:**<br />
<pre>
**Input:** [1,2,3,4,5], k=4, x=3
**Output:** [1,2,3,4]
</pre>


**Example 2:**<br />
<pre>
**Input:** [1,2,3,4,5], k=4, x=-1
**Output:** [1,2,3,4]
</pre>


**Note:**<br>
<ol>
- The value k is positive and will always be smaller than the length of the sorted array.
-  Length of the given array is positive and will not exceed 10<sup>4</sup>
-  Absolute value of elements in the array and x will not exceed 10<sup>4</sup>
</ol>



**<font color="red">UPDATE (2017/9/19):</font>**<br />
The *arr* parameter had been changed to an **array of integers** (instead of a list of integers). ***Please reload the code definition to get the latest changes***.

