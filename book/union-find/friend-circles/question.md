## Friend Circles  
### 链接  
https://leetcode.com/problems/friend-circles/description/  
### 问题描述

There are **N** students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a **direct** friend of B, and B is a **direct** friend of C, then A is an **indirect** friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.



Given a **N*N** matrix **M** representing the friend relationship between students in the class. If M[i][j] = 1, then the i<sub>th</sub> and j<sub>th</sub> students are **direct** friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.


**Example 1:**<br />
<pre>
**Input:** 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
**Output:** 2
**Explanation:**The 0<sub>th</sub> and 1<sub>st</sub> students are direct friends, so they are in a friend circle. <br/>The 2<sub>nd</sub> student himself is in a friend circle. So return 2.
</pre>


**Example 2:**<br />
<pre>
**Input:** 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
**Output:** 1
**Explanation:**The 0<sub>th</sub> and 1<sub>st</sub> students are direct friends, the 1<sub>st</sub> and 2<sub>nd</sub> students are direct friends, <br/>so the 0<sub>th</sub> and 2<sub>nd</sub> students are indirect friends. All of them are in the same friend circle, so return 1.
</pre>


**Note:**<br>
<ol>
- N is in range [1,200].
- M[i][i] = 1 for all students.
- If M[i][j] = 1, then M[j][i] = 1.
</ol>

