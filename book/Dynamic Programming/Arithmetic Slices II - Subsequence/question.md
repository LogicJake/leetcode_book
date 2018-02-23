## Arithmetic Slices II - Subsequence  
### 问题描述
A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

The following sequence is not arithmetic.

A zero-indexed array A consisting of N numbers is given. A **subsequence** slice of that array is any sequence of integers (P<sub>0</sub>, P<sub>1</sub>, ..., P<sub>k</sub>) such that 0 &le; P<sub>0</sub> < P<sub>1</sub> < ... < P<sub>k</sub> < N.

A **subsequence** slice (P<sub>0</sub>, P<sub>1</sub>, ..., P<sub>k</sub>) of array A is called arithmetic if the sequence A[P<sub>0</sub>], A[P<sub>1</sub>], ..., A[P<sub>k-1</sub>], A[P<sub>k</sub>] is arithmetic. In particular, this means that k &ge; 2.

The function should return the number of arithmetic subsequence slices in the array A. 

The input contains N integers. Every integer is in the range of -2<sup>31</sup> and 2<sup>31</sup>-1 and 0 &le; N &le; 1000. The output is guaranteed to be less than 2<sup>31</sup>-1.

**Example:**
<pre>
**Input:** [2, 4, 6, 8, 10]

**Output:** 7

**Explanation:**
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
</pre>

