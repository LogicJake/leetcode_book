

Given two integers `n` and `k`, you need to construct a list which contains `n` different positive integers ranging from `1` to `n` and obeys the following requirement: <br/>

Suppose this list is [a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ... , a<sub>n</sub>], then the list [|a<sub>1</sub> - a<sub>2</sub>|, |a<sub>2</sub> - a<sub>3</sub>|, |a<sub>3</sub> - a<sub>4</sub>|, ... , |a<sub>n-1</sub> - a<sub>n</sub>|] has exactly `k` distinct integers.



If there are multiple answers, print any of them.


**Example 1:**<br/>
<pre>
**Input:** n = 3, k = 1
**Output:** [1, 2, 3]
**Explanation:** The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
</pre>


**Example 2:**<br />
<pre>
**Input:** n = 3, k = 2
**Output:** [1, 3, 2]
**Explanation:** The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
</pre>


**Note:**<br>
<ol>
- The `n` and `k` are in the range 1 <= k < n <= 10<sup>4</sup>.
</ol>

