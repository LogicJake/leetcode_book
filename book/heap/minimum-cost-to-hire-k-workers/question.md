## Minimum Cost to Hire K Workers  
### 链接  
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/  
### 问题描述
There are `N` workers.&nbsp; The `i`-th worker has a `quality[i]` and a minimum wage expectation `wage[i]`.

Now we want to hire exactly `K`&nbsp;workers to form a **paid group**.&nbsp; When hiring a group of K workers, we must pay them according to the following rules:

	1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
	1. Every worker in the paid group must be paid at least their minimum wage expectation.

Return the least amount of money needed to form a paid group satisfying the above conditions.

&nbsp;


**Example 1:**

**Example 2:**

&nbsp;

**Note:**

	1. `1 &lt;= K &lt;= N &lt;= 10000`, where `N = quality.length = wage.length`
	1. `1 &lt;= quality[i] &lt;= 10000`
	1. `1 &lt;= wage[i] &lt;= 10000`
	1. Answers within `10^-5` of the correct answer will be considered correct.
