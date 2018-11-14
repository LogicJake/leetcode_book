## Race Car  
### 链接  
https://leetcode.com/problems/race-car/description/  
### 问题描述
Your car starts at position 0 and speed +1 on an infinite number line.&nbsp; (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction &quot;A&quot;, your car does the following:&nbsp;`position += speed, speed *= 2`.

When you get an instruction &quot;R&quot;, your car does the following: if your speed is positive then&nbsp;`speed = -1`&nbsp;, otherwise&nbsp;`speed = 1`.&nbsp; (Your position stays the same.)

For example, after commands &quot;AAR&quot;, your car goes to positions 0-&gt;1-&gt;3-&gt;3, and your speed goes to 1-&gt;2-&gt;4-&gt;-1.

Now for some target position, say the **length** of the shortest sequence of instructions to get there.

&nbsp;

**Note: **

	- `1 &lt;= target &lt;= 10000`.
