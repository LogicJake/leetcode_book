## Bricks Falling When Hit  
### 链接  
https://leetcode.com/problems/bricks-falling-when-hit/description/  
### 问题描述
We have a grid of 1s and 0s; the 1s in a cell represent bricks.&nbsp; A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures&nbsp;sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may&nbsp;drop because of that&nbsp;erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

&nbsp;

**Note:**

	- The number of rows and columns in the grid will be in the range&nbsp;[1, 200].
	- The number of erasures will not exceed the area of the grid.
	- It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
	- An erasure may refer to a location with no brick - if it does, no bricks drop.
