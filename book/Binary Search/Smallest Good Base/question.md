## Smallest Good Base  
### 问题描述
For an integer n, we call k>=2 a ***good base*** of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format. <br/>

**Example 1:**<br />
<pre>
**Input:** "13"
**Output:** "3"
**Explanation:** 13 base 3 is 111.
</pre>


**Example 2:**<br />
<pre>
**Input:** "4681"
**Output:** "8"
**Explanation:** 4681 base 8 is 11111.
</pre>


**Example 3:**<br />
<pre>
**Input:** "1000000000000000000"
**Output:** "999999999999999999"
**Explanation:** 1000000000000000000 base 999999999999999999 is 11.
</pre>


**Note:**<br>
<ol>
- The range of n is [3, 10^18].
- The string representing n is always valid and will not have leading zeros.
</ol>

