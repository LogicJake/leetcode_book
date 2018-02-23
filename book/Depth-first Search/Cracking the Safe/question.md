## Cracking the Safe  
### 问题描述

There is a box protected by a password.  The password is `n` digits, where each letter can be one of the first `k` digits `0, 1, ..., k-1`.



You can keep inputting the password, the password will automatically be matched against the last `n` digits entered.



For example, assuming the password is `"345"`, I can open it when I type `"012345"`, but I enter a total of 6 digits.



Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.


**Example 1:**<br />
<pre>
**Input:** n = 1, k = 2
**Output:** "01"
**Note:** "10" will be accepted too.
</pre>


**Example 2:**<br />
<pre>
**Input:** n = 2, k = 2
**Output:** "00110"
**Note:** "01100", "10011", "11001" will be accepted too.
</pre>


**Note:**<br>
<ol>
- `n` will be in the range `[1, 4]`.
- `k` will be in the range `[1, 10]`.
- `k^n` will be at most `4096`.
</ol>

