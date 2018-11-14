## Dungeon Game  
### 链接  
https://leetcode.com/problems/dungeon-game/description/  
### 问题描述
The demons had captured the princess (**P**) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (**K**) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (**negative** integers) upon entering these rooms; other rooms are either empty (**0&#39;s**) or contain magic orbs that increase the knight&#39;s health (**positive** integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

&nbsp;

**Write a function to determine the knight&#39;s minimum initial health so that he is able to rescue the princess.**

For example, given the dungeon below, the initial health of the knight must be at least **7** if he follows the optimal path `RIGHT-&gt; RIGHT -&gt; DOWN -&gt; DOWN`.
			|-2 (K)			|-3			|3		
			|-5			|-10			|1		
			|10			|30			|-5 (P)		

&nbsp;

**Note:**

	- The knight&#39;s health has no upper bound.
	- Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
