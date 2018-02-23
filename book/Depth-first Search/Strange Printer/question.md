

There is a strange printer with the following two special requirements:

<ol>
- The printer can only print a sequence of the same character each time.
- At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
</ol>




Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.


**Example 1:**<br />
<pre>
**Input:** "aaabbb"
**Output:** 2
**Explanation:** Print "aaa" first and then print "bbb".
</pre>


**Example 2:**<br />
<pre>
**Input:** "aba"
**Output:** 2
**Explanation:** Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
</pre>


**Hint**: Length of the given string will not exceed 100.
