## Escape The Ghosts  
### 链接  
https://leetcode.com/problems/escape-the-ghosts/description/  
### 问题描述
You are playing a simplified Pacman game. You&nbsp;start at the point `(0, 0)`, and your destination is` (target[0], target[1])`. There are several ghosts on the map, the i-th ghost starts at` (ghosts[i][0], ghosts[i][1])`.

Each turn, you and all ghosts simultaneously *may* move in one of 4 cardinal directions: north, east, west, or south, going from the previous point to a new point 1 unit of distance away.

You escape if and only if you can reach the target before any ghost reaches you (for any given moves the ghosts may take.)&nbsp; If you reach any square (including the target) at the same time as a ghost, it doesn&#39;t count as an escape.

Return True if and only if it is possible to escape.

**Note:**

	- All points have coordinates with absolute value &lt;= `10000`.
	- The number of ghosts will not exceed `100`.
