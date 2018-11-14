## Stone Game  
### 链接  
https://leetcode.com/problems/stone-game/description/  
### 问题描述
Alex and Lee play a game with piles of stones.&nbsp; There are an even number of&nbsp;piles **arranged in a row**, and each pile has a positive integer number of stones `piles[i]`.

The objective of the game is to end with the most&nbsp;stones.&nbsp; The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.&nbsp; Each turn, a player&nbsp;takes the entire pile of stones from either the beginning or the end of the row.&nbsp; This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return `True`&nbsp;if and only if Alex wins the game.

&nbsp;

**Example 1:**

&nbsp;

**Note:**

	1. `2 &lt;= piles.length &lt;= 500`
	1. `piles.length` is even.
	1. `1 &lt;= piles[i] &lt;= 500`
	1. `sum(piles)` is odd.
