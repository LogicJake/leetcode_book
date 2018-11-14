## Online Stock Span  
### 链接  
https://leetcode.com/problems/online-stock-span/description/  
### 问题描述
Write a class `StockSpanner` which collects daily price quotes for some stock, and returns the **span**&nbsp;of that stock&#39;s price for the current day.

The span of the stock&#39;s price today&nbsp;is defined as the maximum number of consecutive days (starting from today and going backwards)&nbsp;for which the price of the stock was less than or equal to today&#39;s price.

For example, if the price of a stock over the next 7 days were `[100, 80, 60, 70, 60, 75, 85]`, then the stock spans would be `[1, 1, 1, 2, 1, 4, 6]`.

&nbsp;

**Example 1:**

&nbsp;

**Note:**

	1. Calls to `StockSpanner.next(int price)` will have `1 &lt;= price &lt;= 10^5`.
	1. There will be at most `10000` calls to `StockSpanner.next`&nbsp;per test case.
	1. There will be at most `150000` calls to `StockSpanner.next` across all test cases.
	1. The total&nbsp;time limit for this problem has been reduced by 75% for&nbsp;C++, and 50% for all other languages.
