## Word Subsets  
### 链接  
https://leetcode.com/problems/word-subsets/description/  
### 问题描述
We are given two arrays `A` and `B` of words.&nbsp; Each word is a string of lowercase letters.

Now, say that&nbsp;word `b` is a subset of word `a`**&nbsp;**if every letter in `b` occurs in `a`, **including multiplicity**.&nbsp; For example, `&quot;wrr&quot;` is a subset of `&quot;warrior&quot;`, but is not a subset of `&quot;world&quot;`.

Now say a word `a` from `A` is **universal** if for every `b` in `B`, `b`&nbsp;is a subset of `a`.&nbsp;

Return a list of all universal words in `A`.&nbsp; You can return the words in any order.

&nbsp;


**Example 1:**

**Example 2:**

**Example 3:**

**Example 4:**

**Example 5:**

&nbsp;

**Note:**

	1. `1 &lt;= A.length, B.length &lt;= 10000`
	1. `1 &lt;= A[i].length, B[i].length&nbsp;&lt;= 10`
	1. `A[i]` and `B[i]` consist only of lowercase letters.
	1. All words in `A[i]` are unique: there isn&#39;t `i != j` with `A[i] == A[j]`.
