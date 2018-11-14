## Student Attendance Record II  
### 链接  
https://leetcode.com/problems/student-attendance-record-ii/description/  
### 问题描述
Given a positive integer **n**, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 10<sup>9</sup> + 7.

A student attendance record is a string that only contains the following three characters:


<ol>
- **'A'** : Absent. 
- **'L'** : Late.
-  **'P'** : Present. 
</ol>



A record is regarded as rewardable if it doesn't contain **more than one 'A' (absent)** or **more than two continuous 'L' (late)**.

**Example 1:**<br />
<pre>
**Input:** n = 2
**Output:** 8 
**Explanation:**
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
</pre>


**Note:**
The value of **n** won't exceed 100,000.

