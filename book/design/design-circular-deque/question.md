## Design Circular Deque  
### 链接  
https://leetcode.com/problems/design-circular-deque/description/  
### 问题描述
Design your implementation of the circular double-ended queue (deque).

Your implementation should support following operations:

	- `MyCircularDeque(k)`: Constructor, set the size of the deque to be k.
	- `insertFront()`: Adds an item at the front of Deque. Return true if the operation is successful.
	- `insertLast()`: Adds an item at the rear of Deque. Return true if the operation is successful.
	- `deleteFront()`: Deletes an item from the front of Deque. Return true if the operation is successful.
	- `deleteLast()`: Deletes an item from the rear of Deque. Return true if the operation is successful.
	- `getFront()`: Gets the front item from the Deque. If the deque is empty, return -1.
	- `getRear()`: Gets the last item from Deque. If the deque is empty, return -1.
	- `isEmpty()`: Checks whether Deque is empty or not.&nbsp;
	- `isFull()`: Checks whether Deque is full or not.

&nbsp;

**Example:**

&nbsp;

**Note:**

	- All values will be in the range of [0, 1000].
	- The number of operations will be in the range of&nbsp;[1, 1000].
	- Please do not use the built-in Deque library.
