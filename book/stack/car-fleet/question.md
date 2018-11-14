## Car Fleet  
### 链接  
https://leetcode.com/problems/car-fleet/description/  
### 问题描述
`N` cars are going to the same destination along a one lane road.&nbsp; The destination is `target`&nbsp;miles away.

Each car `i`&nbsp;has a constant speed `speed[i]`&nbsp;(in miles per hour), and initial position `position[i]`&nbsp;miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A **car fleet** is some non-empty set of cars driving&nbsp;at the same position and same speed.&nbsp; Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will&nbsp;still be&nbsp;considered as one car fleet.

<br />
How many car fleets will arrive at the destination?

&nbsp;

**Example 1:**

<br />
**Note:**

	1. `0 &lt;= N &lt;= 10 ^ 4`
	1. `0 &lt; target&nbsp;&lt;= 10 ^ 6`
	1. `0 &lt;&nbsp;speed[i] &lt;= 10 ^ 6`
	1. `0 &lt;= position[i] &lt; target`
	1. All initial positions are different.
