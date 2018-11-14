## Design Linked List  
### 链接  
https://leetcode.com/problems/design-linked-list/description/  
### 问题描述
Design your&nbsp;implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly&nbsp;linked list should have two attributes: `val`&nbsp;and `next`. `val` is the value of the current node, and `next`&nbsp;is&nbsp;a&nbsp;pointer/reference to the next node. If you want to use the doubly linked list,&nbsp;you will need&nbsp;one more attribute `prev` to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

	- get(index) : Get the value of&nbsp;the `index`-th&nbsp;node in the linked list. If the index is invalid, return `-1`.
	- addAtHead(val) : Add a node of value `val`&nbsp;before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
	- addAtTail(val) : Append a node of value `val`&nbsp;to the last element of the linked list.
	- addAtIndex(index, val) : Add a node of value `val`&nbsp;before the `index`-th&nbsp;node in the linked list.&nbsp;If `index`&nbsp;equals&nbsp;to the length of&nbsp;linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
	- deleteAtIndex(index) : Delete&nbsp;the `index`-th&nbsp;node in the linked list, if the index is valid.

**Example:**

**Note:**

	- All values will be in the range of `[1, 1000]`.
	- The number of operations will be in the range of&nbsp;`[1, 1000]`.
	- Please do not use the built-in LinkedList library.
