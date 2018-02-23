
You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

**Example 1:**<br />
<pre>
**Input:** [1,2,3,3,4,5]
**Output:** True
**Explanation:**
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
</pre>


**Example 2:**<br />
<pre>
**Input:** [1,2,3,3,4,4,5,5]
**Output:** True
**Explanation:**
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
</pre>


**Example 3:**<br />
<pre>
**Input:** [1,2,3,4,4,5]
**Output:** False
</pre>


**Note:**<br>
<ol>
- The length of the input is in range of [1, 10000]
</ol>

