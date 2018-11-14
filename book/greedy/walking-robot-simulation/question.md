## Walking Robot Simulation  
### 链接  
https://leetcode.com/problems/walking-robot-simulation/description/  
### 问题描述
A robot on an infinite grid starts at point (0, 0) and faces north.&nbsp; The robot can receive one of three possible types of commands:

	- `-2`: turn left 90 degrees
	- `-1`: turn right 90 degrees
	- `1 &lt;= x &lt;= 9`: move forward `x` units

Some of the grid squares are obstacles.&nbsp;

The `i`-th obstacle is at grid point `(obstacles[i][0], obstacles[i][1])`

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the **square** of the maximum Euclidean distance that the robot will be from the origin.

&nbsp;

**Example 1:**

**Example 2:**

&nbsp;

**Note:**

	1. `0 &lt;= commands.length &lt;= 10000`
	1. `0 &lt;= obstacles.length &lt;= 10000`
	1. `-30000 &lt;= obstacle[i][0] &lt;= 30000`
	1. `-30000 &lt;= obstacle[i][1] &lt;= 30000`
	1. The answer is guaranteed to be less than `2 ^ 31`.
