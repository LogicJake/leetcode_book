## K-th Smallest Prime Fraction  
### 链接  
https://leetcode.com/problems/k-th-smallest-prime-fraction/description/  
### 问题描述
A sorted list `A` contains 1, plus some number of primes.&nbsp; Then, for every p &lt; q in the list, we consider the fraction p/q.

What is the `K`-th smallest fraction considered?&nbsp; Return your answer as an array of ints, where `answer[0] = p` and `answer[1] = q`.

**Note:**

	- `A` will have length between `2` and `2000`.
	- Each `A[i]` will be between `1` and `30000`.
	- `K` will be between `1` and `A.length * (A.length - 1) / 2`.
