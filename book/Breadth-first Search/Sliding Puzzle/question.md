## Sliding Puzzle  
### 问题描述
On a 2x3 `board`, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing `0`&nbsp;and a 4-directionally adjacent number and swapping it.

The state of the board is **solved** if and only if the `board` is `[[1,2,3],[4,5,0]].`

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

**Examples:**

**Note:**

	- `board` will be a 2 x 3 array as described above.
	- `board[i][j]` will be a permutation of `[0, 1, 2, 3, 4, 5]`.
