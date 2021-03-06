## Evaluate Division  
### 链接  
https://leetcode.com/problems/evaluate-division/description/  
### 问题描述

Equations are given in the format `A / B = k`, where  `A` and `B` are variables represented as strings, and `k` is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return `-1.0`.


**Example:**<br/>
Given ` a / b = 2.0, b / c = 3.0.` <br/>queries are: ` a / c = ?,  b / a = ?, a / e = ?,  a / a = ?, x / x = ? .` <br/>return ` [6.0, 0.5, -1.0, 1.0, -1.0 ].`



The input is: ` vector&lt;pair&lt;string, string&gt;&gt; equations, vector&lt;double&gt;&amp; values, vector&lt;pair&lt;string, string&gt;&gt; queries `, where `equations.size() == values.size()`, and the values are positive. This represents the equations. Return ` vector&lt;double&gt;`.


According to the example above:
<pre>equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. </pre>



The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

