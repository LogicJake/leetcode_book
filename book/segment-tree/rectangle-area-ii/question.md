## Rectangle Area II  
### 链接  
https://leetcode.com/problems/rectangle-area-ii/description/  
### 问题描述
We are given a list of (axis-aligned)&nbsp;`rectangles`.&nbsp; Each&nbsp;`rectangle[i] = [x1, y1, x2, y2]&nbsp;`, where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the `i`th rectangle.

Find the total area covered by all `rectangles` in the plane.&nbsp; Since the answer&nbsp;may be too large, **return it modulo 10^9 + 7**.

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png" style="width: 480px; height: 360px;" />

**Example 1:**

**Example 2:**

**Note:**

	- `1 &lt;= rectangles.length &lt;= 200`
	- `<font face="monospace">rectanges[i].length = 4</font>`
	- `0 &lt;= rectangles[i][j] &lt;= 10^9`
	- The total area covered by all rectangles will never exceed&nbsp;`2^63 - 1`&nbsp;and thus will fit in a 64-bit signed integer.
