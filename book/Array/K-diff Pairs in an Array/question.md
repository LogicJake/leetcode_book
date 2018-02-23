

Given an array of integers and an integer **k**, you need to find the number of **unique** k-diff pairs in the array. Here a **k-diff** pair is defined as an integer pair (i, j), where **i** and **j** are both numbers in the array and their <a href = "https://en.wikipedia.org/wiki/Absolute_difference">absolute difference</a> is **k**.


**Example 1:**<br />
<pre>
**Input:** [3, 1, 4, 1, 5], k = 2
**Output:** 2
**Explanation: **There are two 2-diff pairs in the array, (1, 3) and (3, 5).</br>Although we have two 1s in the input, we should only return the number of **unique** pairs.
</pre>


**Example 2:**<br />
<pre>
**Input:**[1, 2, 3, 4, 5], k = 1
**Output: **4
**Explanation:** There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
</pre>


**Example 3:**<br />
<pre>
**Input: **[1, 3, 1, 5, 4], k = 0
**Output: **1
**Explanation:** There is one 0-diff pair in the array, (1, 1).
</pre>


**Note:**<br>
<ol>
- The pairs (i, j) and (j, i) count as the same pair.
- The length of the array won't exceed 10,000.
- All the integers in the given input belong to the range: [-1e7, 1e7].
</ol>

