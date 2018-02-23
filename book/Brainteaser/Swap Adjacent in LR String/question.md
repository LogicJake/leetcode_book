## Swap Adjacent in LR String  
### 问题描述
In a string composed of `&#39;L&#39;`, `&#39;R&#39;`, and `&#39;X&#39;` characters, like `&quot;RXXLRXRXL&quot;`, a move consists of either replacing one occurrence of `&quot;XL&quot;` with `&quot;LX&quot;`, or replacing one occurrence of `&quot;RX&quot;` with `&quot;XR&quot;`. Given the starting string `start` and the ending string `end`, return `True` if and only if there exists a sequence of moves to transform one string to the other.

**Example:**

**Note:**

	1. `1 &lt;= len(start) = len(end) &lt;= 10000`.
	1. Both start and end will only consist of characters in `{&#39;L&#39;, &#39;R&#39;, &#39;X&#39;}`.
