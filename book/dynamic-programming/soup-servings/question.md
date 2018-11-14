## Soup Servings  
### 链接  
https://leetcode.com/problems/soup-servings/description/  
### 问题描述
There are two types of soup: type A and type B. Initially we have `N` ml of each type of soup. There are four kinds of operations:

	1. Serve&nbsp;100 ml of soup A and 0 ml of soup B
	1. Serve&nbsp;75 ml of soup A and 25&nbsp;ml of soup B
	1. Serve 50 ml of soup A and 50 ml of soup B
	1. Serve 25&nbsp;ml of soup A and 75&nbsp;ml of soup B

When we serve some soup, we give it to someone and we no longer have it.&nbsp; Each turn,&nbsp;we will choose from the four operations with equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve&nbsp;as much as we can.&nbsp; We stop once we no longer have some quantity of both types of soup.

Note that we do not have the operation where all 100 ml&#39;s of soup B are used first.&nbsp;&nbsp;

Return the probability that soup A will be empty&nbsp;first, plus half the probability that A and B become empty at the same time.

&nbsp;

**Notes: **

	- `0 &lt;= N &lt;= 10^9`.&nbsp;
	- Answers within&nbsp;`10^-6`&nbsp;of the true value will be accepted as correct.
