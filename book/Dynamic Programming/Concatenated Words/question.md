## Concatenated Words  
### 问题描述
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

**Example:**<br />
<pre>
**Input:** ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

**Output:** ["catsdogcats","dogcatsdog","ratcatdogcat"]

**Explanation:** "catsdogcats" can be concatenated by "cats", "dog" and "cats"; <br> "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; <br>"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
</pre>


**Note:**<br>
<ol>
<li>The number of elements of the given array will not exceed `10,000 `
- The length sum of elements in the given array will not exceed `600,000`. 
- All the input string will only include lower case letters.
- The returned elements order does not matter. 
</ol>

