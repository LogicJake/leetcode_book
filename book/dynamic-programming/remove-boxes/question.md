## Remove Boxes  
### 链接  
https://leetcode.com/problems/remove-boxes/description/  
### 问题描述
Given several boxes with different colors represented by different positive numbers. <br />
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get `k*k` points.<br />
Find the maximum points you can get.


**Example 1:**<br>
Input: 
<pre>
[1, 3, 2, 2, 2, 3, 4, 3, 1]
</pre>
Output:
<pre>
23
</pre>
Explanation: 
<pre>
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
</pre>


**Note:**
The number of boxes `n` would not exceed 100.

