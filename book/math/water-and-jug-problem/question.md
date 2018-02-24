## Water and Jug Problem  
### 链接  
https://leetcode.com/problems/water-and-jug-problem/description/  
### 问题描述
You are given two jugs with capacities *x* and *y* litres. There is an infinite amount of water supply available.
You need to determine whether it is possible to measure exactly *z* litres using these two jugs.

If *z* liters of water is measurable, you must have *z* liters of water contained within **one or both buckets** by the end.


Operations allowed:
<ul>
- Fill any of the jugs completely with water.
- Empty any of the jugs.
- Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
</ul>


**Example 1:** (From the famous [*"Die Hard"* example](https://www.youtube.com/watch?v=BVtQNK_ZUJg))
<pre>
Input: x = 3, y = 5, z = 4
Output: True
</pre>


**Example 2:**
<pre>
Input: x = 2, y = 6, z = 5
Output: False
</pre>


**Credits:**<br />Special thanks to [@vinod23](https://discuss.leetcode.com/user/vinod23) for adding this problem and creating all test cases.
