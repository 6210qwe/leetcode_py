# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 309
标题: Best Time to Buy and Sell Stock with Cooldown
难度: medium
链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
309. 买卖股票的最佳时机含冷冻期 - 给定一个整数数组prices，其中第 prices[i] 表示第 i 天的股票价格 。 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: * 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 示例 1: 输入: prices = [1,2,3,0,2] 输出: 3 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 示例 2: 输入: prices = [1] 输出: 0 提示： * 1 <= prices.length <= 5000 * 0 <= prices[i] <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 动态规划，维护三个状态：持有股票、不持有股票（冷冻期）、不持有股票（非冷冻期）

算法步骤:
1. hold[i]: 第i天持有股票的最大收益
2. sold[i]: 第i天卖出股票（进入冷冻期）的最大收益
3. rest[i]: 第i天不持有股票且不在冷冻期的最大收益
4. 状态转移：
   - hold[i] = max(hold[i-1], rest[i-1] - prices[i])
   - sold[i] = hold[i-1] + prices[i]
   - rest[i] = max(rest[i-1], sold[i-1])

关键点:
- 使用状态机DP
- 时间复杂度O(n)，空间复杂度O(1)（可优化）
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 需要遍历数组一次
空间复杂度: O(1) - 只使用常数额外空间（优化后）
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def best_time_to_buy_and_sell_stock_with_cooldown(prices: List[int]) -> int:
    """
    函数式接口 - 买卖股票的最佳时机含冷冻期
    
    实现思路:
    动态规划，维护三个状态：持有股票、不持有股票（冷冻期）、不持有股票（非冷冻期）。
    
    Args:
        prices: 股票价格数组
        
    Returns:
        最大利润
        
    Example:
        >>> best_time_to_buy_and_sell_stock_with_cooldown([1, 2, 3, 0, 2])
        3
    """
    if not prices or len(prices) < 2:
        return 0
    
    # 使用滚动数组优化空间
    hold = -prices[0]  # 持有股票
    sold = 0           # 卖出股票（冷冻期）
    rest = 0           # 不持有股票（非冷冻期）
    
    for i in range(1, len(prices)):
        prev_hold = hold
        prev_sold = sold
        prev_rest = rest
        
        hold = max(prev_hold, prev_rest - prices[i])
        sold = prev_hold + prices[i]
        rest = max(prev_rest, prev_sold)
    
    return max(sold, rest)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(best_time_to_buy_and_sell_stock_with_cooldown)
