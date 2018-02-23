
Given an absolute path for a file (Unix-style), simplify it.

For example,<br />
**path** = `"/home/"`, => `"/home"`<br />
**path** = `"/a/./b/../../c/"`, => `"/c"`<br />


[click to show corner cases.](#)


<ul>
<li>Did you consider the case where **path** = `"/../"`?<br />
In this case, you should return `"/"`.</li>
<li>Another corner case is the path might contain multiple slashes `'/'` together, such as `"/home//foo/"`.<br />
In this case, you should ignore redundant slashes and return `"/home/foo"`.</li>

