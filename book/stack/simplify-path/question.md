## Simplify Path  
### 链接  
https://leetcode.com/problems/simplify-path/description/  
### 问题描述
Given an absolute path for a file (Unix-style), simplify it.

For example,<br />
**path** = `&quot;/home/&quot;`, =&gt; `&quot;/home&quot;`<br />
**path** = `&quot;/a/./b/../../c/&quot;`, =&gt; `&quot;/c&quot;`

[click to show corner cases.](#)

**Corner Cases:**

&nbsp;

&nbsp;

	<li>Did you consider the case where **path** = `&quot;/../&quot;`?<br />
	In this case, you should return `&quot;/&quot;`.</li>
	<li>Another corner case is the path might contain multiple slashes `&#39;/&#39;` together, such as `&quot;/home//foo/&quot;`.<br />
	In this case, you should ignore redundant slashes and return `&quot;/home/foo&quot;`.</li>
