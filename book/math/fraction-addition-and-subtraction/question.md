## Fraction Addition and Subtraction  
### 链接  
https://leetcode.com/problems/fraction-addition-and-subtraction/description/  
### 问题描述
Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be <a href = "https://en.wikipedia.org/wiki/Irreducible_fraction">irreducible fraction</a>. If your final result is an integer, say `2`, you need to change it to the format of fraction that has denominator `1`. So in this case, `2` should be converted to `2/1`.

**Example 1:**<br />
<pre>
**Input:**"-1/2+1/2"
**Output:** "0/1"
</pre>


**Example 2:**<br />
<pre>
**Input:**"-1/2+1/2+1/3"
**Output:** "1/3"
</pre>


**Example 3:**<br />
<pre>
**Input:**"1/3-1/2"
**Output:** "-1/6"
</pre>


**Example 4:**<br />
<pre>
**Input:**"5/3+1/3"
**Output:** "2/1"
</pre>


**Note:**<br>
<ol>
- The input string only contains `'0'` to `'9'`, `'/'`, `'+'` and `'-'`. So does the output.
- Each fraction (input and output) has format `±numerator/denominator`. If the first input fraction or the output is positive, then `'+'` will be omitted.
- The input only contains valid **irreducible fractions**, where the **numerator** and **denominator** of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above. 
- The number of given fractions will be in the range [1,10].
- The numerator and denominator of the **final result** are guaranteed to be valid and in the range of 32-bit int.
</ol>

