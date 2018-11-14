## Number of Recent Calls  
### 链接  
https://leetcode.com/problems/number-of-recent-calls/description/  
### 问题描述
Write a class `RecentCounter` to count recent requests.

It has only one method:&nbsp;`ping(int t)`, where t represents some time in milliseconds.

Return the number of `ping`s that have been made from 3000 milliseconds ago until now.

Any ping with time in `[t - 3000, t]` will count, including the current ping.

It is guaranteed that every call to `ping` uses a strictly larger value of&nbsp;`t` than before.

&nbsp;

**Example 1:**

&nbsp;

**Note:**

	1. Each test case will have at most `10000` calls to `ping`.
	1. Each test case will call&nbsp;`ping` with strictly increasing values of `t`.
	1. Each call to ping will have `1 &lt;= t &lt;= 10^9`.

&nbsp;
