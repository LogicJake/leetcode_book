## Shortest Path to Get All Keys  
### 链接  
https://leetcode.com/problems/shortest-path-to-get-all-keys/description/  
### 问题描述
We are given a 2-dimensional&nbsp;`grid`.&nbsp;`&quot;.&quot;` is an empty cell, `&quot;#&quot;` is&nbsp;a wall, `&quot;@&quot;` is the starting point, (`&quot;a&quot;`, `&quot;b&quot;`, ...) are keys, and (`&quot;A&quot;`,&nbsp;`&quot;B&quot;`, ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.&nbsp; We cannot walk outside the grid, or walk into a wall.&nbsp; If we walk over a key, we pick it up.&nbsp; We can&#39;t walk over a lock unless we have the corresponding key.

For some <font face="monospace">1 &lt;= K &lt;= 6</font>, there is exactly one lowercase and one uppercase letter of the first `K` letters of the English alphabet in the grid.&nbsp; This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were&nbsp;chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.&nbsp; If&nbsp;it&#39;s impossible, return `-1`.

&nbsp;

**Example 1:**

**Example 2:**

&nbsp;

**Note:**

	1. `1 &lt;= grid.length&nbsp;&lt;= 30`
	1. `1 &lt;= grid[0].length&nbsp;&lt;= 30`
	1. `grid[i][j]` contains only` &#39;.&#39;`, `&#39;#&#39;`, `&#39;@&#39;`,&nbsp;`&#39;a&#39;-``&#39;f``&#39;` and `&#39;A&#39;-&#39;F&#39;`
	1. The number of keys is in `[1, 6]`.&nbsp; Each key has a different letter and opens exactly one lock.
