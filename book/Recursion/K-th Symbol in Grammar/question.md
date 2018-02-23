
On the first row, we write a `0`. Now in every subsequent row, we look at the previous row and replace each occurrence of `0` with `01`, and each occurrence of `1` with `10`.

Given row `N` and index `K`, return the `K`-th indexed symbol in row `N`. (The values of `K` are 1-indexed.) (1 indexed).

**Note:**

	1. `N` will be an integer in the range `[1, 30]`.
	1. `K` will be an integer in the range `[1, 2^(N-1)]`.
