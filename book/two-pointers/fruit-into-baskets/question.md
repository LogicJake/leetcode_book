## Fruit Into Baskets  
### 链接  
https://leetcode.com/problems/fruit-into-baskets/description/  
### 问题描述
In a row of trees, the `i`-th tree&nbsp;produces&nbsp;fruit with type&nbsp;`tree[i]`.

You **start at any tree&nbsp;of your choice**, then repeatedly perform the following steps:

	1. Add one piece of fruit from this tree to your baskets.&nbsp; If you cannot, stop.
	1. Move to the next tree to the right of the current tree.&nbsp; If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree:&nbsp;you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

&nbsp;

**Example 1:**

**Example 2:**

**Example 3:**

**Example 4:**

&nbsp;

**Note:**

	1. `1 &lt;= tree.length &lt;= 40000`
	1. `0 &lt;= tree[i] &lt; tree.length`
