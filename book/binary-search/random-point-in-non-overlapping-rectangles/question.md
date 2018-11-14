## Random Point in Non-overlapping Rectangles  
### 链接  
https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/description/  
### 问题描述
Given a list of **non-overlapping**&nbsp;axis-aligned rectangles `rects`, write a function `pick` which randomly and uniformily picks an **integer point** in the space&nbsp;covered by the rectangles.

Note:

	1. An **integer point**&nbsp;is a point that has integer coordinates.&nbsp;
	1. A point&nbsp;on the perimeter&nbsp;of a rectangle is&nbsp;**included** in the space covered by the rectangles.&nbsp;
	1. `i`th rectangle = `rects[i]` =&nbsp;`[x1,y1,x2,y2]`, where `[x1, y1]`&nbsp;are the integer coordinates of the bottom-left corner, and `[x2, y2]`&nbsp;are the integer coordinates of the top-right corner.
	1. length and width of each rectangle does not exceed `2000`.
	1. `1 &lt;= rects.length&nbsp;&lt;= 100`
	1. `pick` return a point as an array of integer coordinates&nbsp;`[p_x, p_y]`
	1. `pick` is called at most `10000`&nbsp;times.

**Example 1:**

**Example 2:**

**Explanation of Input Syntax:**

The input is two lists:&nbsp;the subroutines called&nbsp;and their&nbsp;arguments.&nbsp;`Solution`&#39;s&nbsp;constructor has one argument, the array of rectangles `rects`. `pick`&nbsp;has no arguments.&nbsp;Arguments&nbsp;are&nbsp;always wrapped with a list, even if there aren&#39;t any.
