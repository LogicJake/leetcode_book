## Friends Of Appropriate Ages  
### 链接  
https://leetcode.com/problems/friends-of-appropriate-ages/description/  
### 问题描述
Some people will make friend requests. The&nbsp;list of their ages is given and&nbsp;`ages[i]`&nbsp;is the age of the&nbsp;ith person.&nbsp;

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

	- `age[B]&nbsp;&lt;= 0.5 * age[A]&nbsp;+ 7`
	- `age[B]&nbsp;&gt; age[A]`
	- `age[B]&nbsp;&gt; 100 &amp;&amp;&nbsp;age[A]&nbsp;&lt; 100`

Otherwise, A will friend request B.

Note that if&nbsp;A requests B, B does not necessarily request A.&nbsp; Also, people will not friend request themselves.

How many total friend requests are made?

**Example 1:**

**Example 2:**

**Example 3:**

&nbsp;

Notes:

	- `1 &lt;= ages.length&nbsp;&lt;= 20000`.
	- `1 &lt;= ages[i] &lt;= 120`.
