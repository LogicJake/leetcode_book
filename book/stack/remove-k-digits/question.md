## Remove K Digits  
### 链接  
https://leetcode.com/problems/remove-k-digits/description/  
### 问题描述
Given a non-negative integer *num* represented as a string, remove *k* digits from the number so that the new number is the smallest possible.


**Note:**<br />
<ul>
- The length of *num* is less than 10002 and will be &ge; *k*.
- The given *num* does not contain any leading zero.
</ul>
</b>


**Example 1:**
<pre>
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
</pre>


**Example 2:**
<pre>
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
</pre>


**Example 3:**
<pre>
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
</pre>

