## Goat Latin  
### 链接  
https://leetcode.com/problems/goat-latin/description/  
### 问题描述
A sentence `S` is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to &quot;**Goat Latin&quot;**&nbsp;(a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

	<li>If a word begins with a vowel (a, e, i, o, or u), append `&quot;ma&quot;`&nbsp;to the end of the word.<br />
	For example, the word &#39;apple&#39; becomes &#39;applema&#39;.<br />
	&nbsp;</li>
	<li>If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add `&quot;ma&quot;`.<br />
	For example, the word `&quot;goat&quot;`&nbsp;becomes `&quot;oatgma&quot;`.<br />
	&nbsp;</li>
	<li>Add one letter `&#39;a&#39;`&nbsp;to the end of each word per its word index in the sentence, starting with 1.<br />
	For example,&nbsp;the first word gets `&quot;a&quot;` added to the end, the second word gets `&quot;aa&quot;` added to the end and so on.</li>

Return the&nbsp;final sentence representing the conversion from `S`&nbsp;to Goat&nbsp;Latin.&nbsp;

&nbsp;

**Example 1:**

**Example 2:**

&nbsp;

Notes:

	- `S` contains only uppercase, lowercase and spaces.&nbsp;Exactly one space between each word.
	- `1 &lt;= S.length &lt;= 150`.
