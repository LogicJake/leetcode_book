## Basic Calculator IV  
### 链接  
https://leetcode.com/problems/basic-calculator-iv/description/  
### 问题描述
Given an `expression`&nbsp;such as `expression = &quot;e + 8 - a + 5&quot;` and an evaluation map such as `{&quot;e&quot;: 1}` (given in terms of `evalvars = [&quot;e&quot;]` and `evalints = [1]`), return a list of tokens representing the simplified expression, such as `[&quot;-1*a&quot;,&quot;14&quot;]`

	- An expression alternates chunks and symbols, with a space separating each chunk and symbol.
	- A chunk is either an expression in parentheses, a variable, or a non-negative integer.
	- A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like `&quot;2x&quot;` or `&quot;-x&quot;`.

Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction. For example, `expression = &quot;1 + 2 * 3&quot;` has an answer of `[&quot;7&quot;]`.

The format of the output is as follows:

	- For each term of free variables with non-zero coefficient, we write the free variables within a term in sorted order lexicographically. For example, we would never write a term like `&quot;b*a*c&quot;`, only `&quot;a*b*c&quot;`.
	- Terms have degree equal to the number of free variables being multiplied, counting multiplicity. (For example, `&quot;a*a*b*c&quot;` has degree 4.) We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
	- The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.)&nbsp; A leading coefficient of 1 is still printed.
	- An example of a well formatted answer is `[&quot;-2*a*a*a&quot;, &quot;3*a*a*b&quot;, &quot;3*b*b&quot;, &quot;4*a&quot;, &quot;5*c&quot;, &quot;-6&quot;]`&nbsp;
	- Terms (including constant terms) with coefficient 0 are not included.&nbsp; For example, an expression of &quot;0&quot; has an output of [].

**Examples:**

**Note:**

	1. `expression` will have length in range `[1, 250]`.
	1. `evalvars, evalints` will have equal lengths in range `[0, 100]`.
