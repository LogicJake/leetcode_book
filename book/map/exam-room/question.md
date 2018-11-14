## Exam Room  
### 链接  
https://leetcode.com/problems/exam-room/description/  
### 问题描述
In an exam room, there are `N` seats in a single row, numbered `0, 1, 2, ..., N-1`.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.&nbsp; If there are multiple such seats, they sit in the seat with the lowest number.&nbsp; (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class `ExamRoom(int N)`&nbsp;that exposes two functions: `ExamRoom.seat()`&nbsp;returning an `int`&nbsp;representing what seat the student sat in, and `ExamRoom.leave(int p)`&nbsp;representing that the student in seat number `p`&nbsp;now leaves the room.&nbsp; It is guaranteed that any calls to `ExamRoom.leave(p)` have a student sitting in seat `p`.

&nbsp;

**Example 1:**

​​​​​​​

**Note:**

	1. `1 &lt;= N &lt;= 10^9`
	1. `ExamRoom.seat()` and `ExamRoom.leave()` will be called at most `10^4` times across all test cases.
	1. Calls to `ExamRoom.leave(p)` are guaranteed to have a student currently sitting in seat number `p`.
