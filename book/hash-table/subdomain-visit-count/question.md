## Subdomain Visit Count  
### 链接  
https://leetcode.com/problems/subdomain-visit-count/description/  
### 问题描述
A website domain like &quot;discuss.leetcode.com&quot; consists of various subdomains. At the top level, we have &quot;com&quot;, at the next level, we have &quot;leetcode.com&quot;, and at the lowest level, &quot;discuss.leetcode.com&quot;. When we visit a domain like &quot;discuss.leetcode.com&quot;, we will also visit the parent domains &quot;leetcode.com&quot; and &quot;com&quot; implicitly.

Now, call a &quot;count-paired domain&quot; to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be &quot;9001 discuss.leetcode.com&quot;.

We are given a list `cpdomains` of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.

**Notes: **

	- The length of `cpdomains` will not exceed&nbsp;`100`.&nbsp;
	- The length of each domain name will not exceed `100`.
	- Each address will have either 1 or 2 &quot;.&quot; characters.
	- The input count&nbsp;in any count-paired domain will not exceed `10000`.
	- The answer output can be returned in any order.
