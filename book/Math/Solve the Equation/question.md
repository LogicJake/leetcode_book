## Solve the Equation  
### 问题描述

Solve a given equation and return the value of `x` in the form of string "x=#value". The equation contains only '+', '-' operation, the variable `x` and its coefficient.



If there is no solution for the equation, return "No solution".



If there are infinite solutions for the equation, return "Infinite solutions".



If there is exactly one solution for the equation, we ensure that the value of `x` is an integer.


**Example 1:**<br/>
<pre>
**Input:** "x+5-3+x=6+x-2"
**Output:** "x=2"
</pre>


**Example 2:**<br/>
<pre>
**Input:** "x=x"
**Output:** "Infinite solutions"
</pre>


**Example 3:**<br/>
<pre>
**Input:** "2x=x"
**Output:** "x=0"
</pre>


**Example 4:**<br/>
<pre>
**Input:** "2x+3x-6x=x+2"
**Output:** "x=-1"
</pre>


**Example 5:**<br/>
<pre>
**Input:** "x=x+2"
**Output:** "No solution"
</pre>

