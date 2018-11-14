## Cat and Mouse  
### 链接  
https://leetcode.com/problems/cat-and-mouse/description/  
### 问题描述
A game on an **undirected** graph is played by two players, Mouse and Cat, who alternate turns.

The graph is given as follows: `graph[a]` is a list of all nodes `b` such that `ab` is an edge of the graph.

Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.

During each player&#39;s turn, they **must** travel along one&nbsp;edge of the graph that meets where they are.&nbsp; For example, if the Mouse is at node `1`, it **must** travel to any node in `graph[1]`.

Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)

Then, the game can end in 3 ways:

	- If ever the Cat occupies the same node as the Mouse, the Cat wins.
	- If ever the Mouse reaches the Hole, the Mouse wins.
	- If ever a position is repeated (ie.&nbsp;the players are in the same position as a previous turn, and&nbsp;it is the same player&#39;s turn to move), the game is a draw.

Given a `graph`, and assuming both players play optimally, return `1`&nbsp;if the game is won by Mouse, `2`&nbsp;if the game is won by Cat, and `0`&nbsp;if the game is a draw.

&nbsp;


**Example 1:**

&nbsp;

**Note:**

	1. `3 &lt;= graph.length &lt;= 50`
	1. It is guaranteed that `graph[1]` is non-empty.
	1. It is guaranteed that `graph[2]` contains a non-zero element.&nbsp;
