## Non-overlapping Intervals  
### 链接  
https://leetcode.com/problems/non-overlapping-intervals/description/  
### 问题描述

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.


**Note:**<br />
<ol>
- You may assume the interval's end point is always bigger than its start point.
- Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
</ol>


**Example 1:**<br />
<pre>
**Input:** [ [1,2], [2,3], [3,4], [1,3] ]

**Output:** 1

**Explanation:** [1,3] can be removed and the rest of intervals are non-overlapping.
</pre>


**Example 2:**<br />
<pre>
**Input:** [ [1,2], [1,2], [1,2] ]

**Output:** 2

**Explanation:** You need to remove two [1,2] to make the rest of intervals non-overlapping.
</pre>


**Example 3:**<br />
<pre>
**Input:** [ [1,2], [2,3] ]

**Output:** 0

**Explanation:** You don't need to remove any of the intervals since they're already non-overlapping.
</pre>

