

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
<ol>
- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string.
- An empty string is also valid.
</ol>


**Example 1:**<br />
<pre>
**Input:** "()"
**Output:** True
</pre>


**Example 2:**<br />
<pre>
**Input:** "(*)"
**Output:** True
</pre>


**Example 3:**<br />
<pre>
**Input:** "(*))"
**Output:** True
</pre>


**Note:**<br>
<ol>
- The string size will be in the range [1, 100].
</ol>

