## 1-bit and 2-bit Characters  
### 链接  
https://leetcode.com/problems/1-bit-and-2-bit-characters/description/  
### 问题描述
We have two special characters. The first character can be represented by one bit `0`. The second character can be represented by two bits (`10` or `11`).  

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

**Example 1:**<br />
<pre>
**Input:** 
bits = [1, 0, 0]
**Output:** True
**Explanation:** 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
</pre>


**Example 2:**<br />
<pre>
**Input:** 
bits = [1, 1, 1, 0]
**Output:** False
**Explanation:** 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
</pre>


**Note:**
- `1 <= len(bits) <= 1000`.
- `bits[i]` is always `0` or `1`.

