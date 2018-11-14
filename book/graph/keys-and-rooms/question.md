## Keys and Rooms  
### 链接  
https://leetcode.com/problems/keys-and-rooms/description/  
### 问题描述
There are `N` rooms and you start in room `0`.&nbsp; Each room has a distinct number in `0, 1, 2, ..., N-1`, and each room may have&nbsp;some keys to access the next room.&nbsp;

Formally, each room `i`&nbsp;has a list of keys `rooms[i]`, and each key `rooms[i][j]` is an integer in `[0, 1, ..., N-1]` where `N = rooms.length`.&nbsp; A key `rooms[i][j] = v`&nbsp;opens the room with number `v`.

Initially, all the rooms start locked (except for room `0`).&nbsp;

You can walk back and forth between rooms freely.

Return `true`&nbsp;if and only if you can enter&nbsp;every room.


**Example 1:**

**Example 2:**

**Note:**

	1. `1 &lt;= rooms.length &lt;=&nbsp;1000`
	1. `0 &lt;= rooms[i].length &lt;= 1000`
	1. The number of keys in all rooms combined is at most&nbsp;`3000`.
