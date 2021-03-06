## Split Array Largest Sum  
### 链接  
https://leetcode.com/problems/split-array-largest-sum/description/  
### 问题描述
Given an array which consists of non-negative integers and an integer *m*, you can split the array into *m* non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these *m* subarrays.


**Note:**<br />
If *n* is the length of array, assume the following constraints are satisfied:
<ul>
- 1 &le; *n* &le; 1000
- 1 &le; *m* &le; min(50, *n*)
</ul>


**Examples: **
<pre>
Input:
**nums** = [7,2,5,10,8]
**m** = 2

Output:
18

Explanation:
There are four ways to split **nums** into two subarrays.
The best way is to split it into **[7,2,5]** and **[10,8]**,
where the largest sum among the two subarrays is only 18.
</pre>

