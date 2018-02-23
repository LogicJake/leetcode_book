## 132 Pattern  
### 问题描述

Given a sequence of n integers a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>, a 132 pattern is a subsequence a<sub>**i**</sub>, a<sub>**j**</sub>, a<sub>**k**</sub> such
that **i** < **j** < **k** and a<sub>**i**</sub> < a<sub>**k**</sub> < a<sub>**j**</sub>. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

**Note:** n will be less than 15,000.

**Example 1:**<br />
<pre>
**Input:** [1, 2, 3, 4]

**Output:** False

**Explanation:** There is no 132 pattern in the sequence.
</pre>


**Example 2:**<br />
<pre>
**Input:** [3, 1, 4, 2]

**Output:** True

**Explanation:** There is a 132 pattern in the sequence: [1, 4, 2].
</pre>


**Example 3:**<br />
<pre>
**Input:** [-1, 3, 2, 0]

**Output:** True

**Explanation:** There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
</pre>

