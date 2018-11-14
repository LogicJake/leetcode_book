## Burst Balloons  
### 链接  
https://leetcode.com/problems/burst-balloons/description/  
### 问题描述
Given `n` balloons, indexed from `0` to `n-1`. Each balloon is painted with a number on it represented by array `nums`. You are asked to burst all the balloons. If the you burst balloon `i` you will get `nums[left] * nums[i] * nums[right]` coins. Here `left` and `right` are adjacent indices of `i`. After the burst, the `left` and `right` then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

**Note:**

	- You may imagine `nums[-1] = nums[n] = 1`. They are not real therefore you can not burst them.
	- 0 &le; `n` &le; 500, 0 &le; `nums[i]` &le; 100

**Example:**
