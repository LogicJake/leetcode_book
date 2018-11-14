## Image Overlap  
### 链接  
https://leetcode.com/problems/image-overlap/description/  
### 问题描述
Two images `A` and `B` are given, represented as&nbsp;binary, square matrices of the same size.&nbsp; (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.&nbsp; After, the **overlap** of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does **not** include any kind of rotation.)

What is the largest possible overlap?

**Example 1:**

**Notes:**&nbsp;

	1. `1 &lt;= A.length = A[0].length = B.length = B[0].length &lt;= 30`
	1. `0 &lt;=&nbsp;A[i][j], B[i][j] &lt;= 1`
