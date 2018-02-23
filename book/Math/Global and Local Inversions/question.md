
We have some permutation `A` of `[0, 1, ..., N - 1]`, where `N` is the length of `A`.

The number of (global) inversions is the number of `i &lt; j` with `0 &lt;= i &lt; j &lt; N` and `A[i] &gt; A[j]`.

The number of local inversions is the number of `i` with `0 &lt;= i &lt; N` and `A[i] &gt; A[i+1]`.

Return `true`&nbsp;if and only if the number of global inversions is equal to the number of local inversions.

**Example 1:**

**Example 2:**

**Note:**

	- `A` will be a permutation of `[0, 1, ..., A.length - 1]`.
	- `A` will have length in range `[1, 5000]`.
	- The time limit for this problem has been reduced.
