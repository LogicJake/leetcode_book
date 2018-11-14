## Masking Personal Information  
### 链接  
https://leetcode.com/problems/masking-personal-information/description/  
### 问题描述
We are given a&nbsp;personal information string `S`, which may represent&nbsp;either **an email address** or **a phone number.**

We would like to mask this&nbsp;personal information according to the&nbsp;following rules:

<br />
<u>**1. Email address:**</u>

We define a&nbsp;**name** to be a string of `length &ge; 2` consisting&nbsp;of only lowercase letters&nbsp;`a-z` or uppercase&nbsp;letters&nbsp;`A-Z`.

An email address starts with a name, followed by the&nbsp;symbol `&#39;@&#39;`, followed by a name, followed by the&nbsp;dot&nbsp;`&#39;.&#39;`&nbsp;and&nbsp;followed by a name.&nbsp;

All email addresses are&nbsp;guaranteed to be valid and in the format of&nbsp;`&quot;name1@name2.name3&quot;.`

To mask an email, **all names must be converted to lowercase** and **all letters between the first and last letter of the first name** must be replaced by 5 asterisks `&#39;*&#39;`.

<br />
<u>**2. Phone number:**</u>

A phone number is a string consisting of&nbsp;only the digits `0-9` or the characters from the set `{&#39;+&#39;, &#39;-&#39;, &#39;(&#39;, &#39;)&#39;, &#39;&nbsp;&#39;}.`&nbsp;You may assume a phone&nbsp;number contains&nbsp;10 to 13 digits.

The last 10 digits make up the local&nbsp;number, while the digits before those make up the country code. Note that&nbsp;the country code is optional. We want to expose only the last 4 digits&nbsp;and mask all other&nbsp;digits.

The local&nbsp;number&nbsp;should be formatted and masked as `&quot;***-***-1111&quot;,&nbsp;`where `1` represents the exposed digits.

To mask a phone number with country code like `&quot;+111 111 111 1111&quot;`, we write it in the form `&quot;+***-***-***-1111&quot;.`&nbsp; The `&#39;+&#39;`&nbsp;sign and the first `&#39;-&#39;`&nbsp;sign before the local number should only exist if there is a country code.&nbsp; For example, a 12 digit phone number mask&nbsp;should start&nbsp;with `&quot;+**-&quot;`.

Note that extraneous characters like `&quot;(&quot;, &quot;)&quot;, &quot; &quot;`, as well as&nbsp;extra dashes or plus signs not part of the above formatting scheme should be removed.

&nbsp;

Return the correct &quot;mask&quot; of the information provided.

&nbsp;

**Example 1:**

**Example 2:**

**Example 3:**

**Example 4:**

**Notes:**

	1. `S.length&nbsp;&lt;=&nbsp;40`.
	1. Emails have length at least 8.
	1. Phone numbers have length at least 10.
