## Smallest Range  
### 问题描述
You have `k` lists of sorted integers in ascending order. Find the **smallest** range that includes at least one number from each of the `k` lists. 

We define the range [a,b] is smaller than range [c,d] if `b-a < d-c` or `a < c` if `b-a == d-c`.

**Example 1:**<br />
<pre>
**Input:**[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
**Output:** [20,24]
**Explanation:** 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
</pre>



**Note:**<br/>
<ol>
- The given list may contain duplicates, so ascending order means >= here.
- 1 <= `k` <= 3500
-  -10<sup>5</sup> <= `value of elements` <= 10<sup>5</sup>.
- **For Java users, please note that the input type has been changed to List&lt;List&lt;Integer&gt;&gt;. And after you reset the code template, you'll see this point.**
</ol>
<br/>

