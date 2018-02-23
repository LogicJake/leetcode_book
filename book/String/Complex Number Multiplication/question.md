## Complex Number Multiplication  
### 问题描述

Given two strings representing two <a href = "https://en.wikipedia.org/wiki/Complex_number">complex numbers</a>.


You need to return a string representing their multiplication. Note i<sup>2</sup> = -1 according to the definition.


**Example 1:**<br />
<pre>
**Input:** "1+1i", "1+1i"
**Output:** "0+2i"
**Explanation:** (1 + i) * (1 + i) = 1 + i<sup>2</sup> + 2 * i = 2i, and you need convert it to the form of 0+2i.
</pre>


**Example 2:**<br />
<pre>
**Input:** "1+-1i", "1+-1i"
**Output:** "0+-2i"
**Explanation:** (1 - i) * (1 - i) = 1 + i<sup>2</sup> - 2 * i = -2i, and you need convert it to the form of 0+-2i.
</pre>


**Note:**
<ol>
- The input strings will not have extra blank.
- The input strings will be given in the form of **a+bi**, where the integer **a** and **b** will both belong to the range of [-100, 100]. And **the output should be also in this form**.
</ol>

