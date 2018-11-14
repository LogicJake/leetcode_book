## Stamping The Sequence  
### 链接  
https://leetcode.com/problems/stamping-the-sequence/description/  
### 问题描述
You want to form a `target`&nbsp;string of **lowercase letters**.

At the beginning, your sequence is `target.length`&nbsp;`&#39;?&#39;` marks.&nbsp; You also have a `stamp`&nbsp;of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.&nbsp; You can make up to `10 * target.length` turns.

For example, if the initial sequence is <font face="monospace">&quot;?????&quot;</font>, and your stamp is `&quot;abc&quot;`,&nbsp; then you may make <font face="monospace">&quot;abc??&quot;, &quot;?abc?&quot;, &quot;??abc&quot;&nbsp;</font>in the first turn.&nbsp; (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of&nbsp;the index of the left-most letter being stamped at each turn.&nbsp; If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is <font face="monospace">&quot;ababc&quot;</font>, and the stamp is `&quot;abc&quot;`, then we could return the answer `[0, 2]`, corresponding to the moves <font face="monospace">&quot;?????&quot; -&gt; &quot;abc??&quot; -&gt; &quot;ababc&quot;</font>.

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within `10 * target.length`&nbsp;moves.&nbsp; Any answers specifying more than this number of moves&nbsp;will not be accepted.

&nbsp;

**Example 1:**

**Example 2:**

&nbsp;

**Note:**

	1. `1 &lt;= stamp.length &lt;= target.length &lt;= 1000`
	1. `stamp` and `target` only contain lowercase letters.
