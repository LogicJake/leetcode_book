## Maximum Frequency Stack  
### 链接  
https://leetcode.com/problems/maximum-frequency-stack/description/  
### 问题描述
Implement `FreqStack`, a class which simulates the operation of a stack-like data structure.

`FreqStack`&nbsp;has two functions:

	- `push(int x)`, which pushes an integer `x` onto the stack.
	<li>`pop()`, which **removes** and returns the most frequent element in the stack.
	<ul>
		- If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
	
&nbsp;

**Example 1:**

&nbsp;

**Note:**

	- Calls to `FreqStack.push(int x)`&nbsp;will be such that `0 &lt;= x &lt;= 10^9`.
	- It is guaranteed that `FreqStack.pop()` won&#39;t be called if the stack has zero elements.
	- The total number of `FreqStack.push` calls will not exceed `10000` in a single test case.
	- The total number of `FreqStack.pop`&nbsp;calls will not exceed `10000` in a single test case.
	- The total number of `FreqStack.push` and `FreqStack.pop` calls will not exceed `150000` across all test cases.

&nbsp;
