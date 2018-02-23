## Find K Pairs with Smallest Sums  
### 问题描述

You are given two integer arrays **nums1** and **nums2** sorted in ascending order and an integer **k**. 


Define a pair **(u,v)** which consists of one element from the first array and one element from the second array.

Find the k pairs **(u<sub>1</sub>,v<sub>1</sub>),(u<sub>2</sub>,v<sub>2</sub>) ...(u<sub>k</sub>,v<sub>k</sub>)** with the smallest sums.


**Example 1:**<br />
<pre>
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>


**Example 2:**<br />
<pre>
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>


**Example 3:**<br />
<pre>
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
</pre>


**Credits:**<br />Special thanks to [@elmirap](https://leetcode.com/elmirap/) and [@StefanPochmann](https://leetcode.com/stefanpochmann/) for adding this problem and creating all test cases.
