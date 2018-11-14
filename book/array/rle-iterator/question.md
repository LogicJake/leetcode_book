## RLE Iterator  
### 链接  
https://leetcode.com/problems/rle-iterator/description/  
### 问题描述
Write an iterator that iterates through a run-length encoded sequence.

The iterator is initialized by `RLEIterator(int[] A)`, where `A` is a run-length encoding of some&nbsp;sequence.&nbsp; More specifically,&nbsp;for all even `i`,&nbsp;`A[i]` tells us the number of times that the non-negative integer value `A[i+1]` is repeated in the sequence.

The iterator supports one function:&nbsp;`next(int n)`, which exhausts the next `n` elements&nbsp;(`n &gt;= 1`) and returns the last element exhausted in this way.&nbsp; If there is no element left to exhaust, `next`&nbsp;returns `-1` instead.

For example, we start with `A = [3,8,0,9,2,5]`, which is a run-length encoding of the sequence `[8,8,8,5,5]`.&nbsp; This is because the sequence can be read as&nbsp;&quot;three eights, zero nines, two fives&quot;.

&nbsp;

**Example 1:**

**Note:**

	1. `0 &lt;= A.length &lt;= 1000`
	1. `A.length`&nbsp;is an even integer.
	1. `0 &lt;= A[i] &lt;= 10^9`
	1. There are at most `1000` calls to `RLEIterator.next(int n)` per test case.
	1. Each call to&nbsp;`RLEIterator.next(int n)`&nbsp;will have `1 &lt;= n &lt;= 10^9`.
