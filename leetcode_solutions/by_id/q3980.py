# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3980
标题: Best Time to Buy and Sell Stock using Strategy
难度: medium
链接: https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-using-strategy/
题目类型: 数组、前缀和、滑动窗口
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3652. 按策略买卖股票的最佳时机 - 给你两个整数数组 prices 和 strategy，其中： * prices[i] 表示第 i 天某股票的价格。 * strategy[i] 表示第 i 天的交易策略，其中： * -1 表示买入一单位股票。 * 0 表示持有股票。 * 1 表示卖出一单位股票。 同时给你一个 偶数 整数 k，你可以对 strategy 进行 最多一次 修改。一次修改包括： * 选择 strategy 中恰好 k 个 连续 元素。 * 将前 k / 2 个元素设为 0（持有）。 * 将后 k / 2 个元素设为 1（卖出）。 利润 定义为所有天数中 strategy[i] * prices[i] 的 总和 。 返回你可以获得的 最大 可能利润。 注意： 没有预算或股票持有数量的限制，因此所有买入和卖出操作均可行，无需考虑过去的操作。 示例 1： 输入： prices = [4,2,8], strategy = [-1,0,1], k = 2 输出： 10 解释： 修改 策略 利润计算 利润 原始 [-1, 0, 1] (-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8 4 修改 [0, 1] [0, 1, 1] (0 × 4) + (1 × 2) + (1 × 8) = 0 + 2 + 8 10 修改 [1, 2] [-1, 0, 1] (-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 8 4 因此，最大可能利润是 10，通过修改子数组 [0, 1] 实现。 示例 2： 输入： prices = [5,4,3], strategy = [1,1,0], k = 2 输出： 9 解释： 修改 策略 利润计算 利润 原始 [1, 1, 0] (1 × 5) + (1 × 4) + (0 × 3) = 5 + 4 + 0 9 修改 [0, 1] [0, 1, 0] (0 × 5) + (1 × 4) + (0 × 3) = 0 + 4 + 0 4 修改 [1, 2] [1, 0, 1] (1 × 5) + (0 × 4) + (1 × 3) = 5 + 0 + 3 8 因此，最大可能利润是 9，无需任何修改即可达成。 提示： * 2 <= prices.length == strategy.length <= 105 * 1 <= prices[i] <= 105 * -1 <= strategy[i] <= 1 * 2 <= k <= prices.length * k 是偶数
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用滑动窗口来计算在每个可能的 k 个连续元素上的最大利润增益。

算法步骤:
1. 计算原始策略下的总利润。
2. 使用滑动窗口遍历所有可能的 k 个连续元素，计算修改后的利润增益。
3. 更新最大利润增益。
4. 返回原始利润加上最大利润增益。

关键点:
- 使用滑动窗口来高效地计算每个 k 个连续元素的利润增益。
- 保持代码简洁和可读性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_profit_with_strategy(prices: List[int], strategy: List[int], k: int) -> int:
    n = len(prices)
    original_profit = sum(p * s for p, s in zip(prices, strategy))
    
    max_gain = 0
    current_gain = 0
    
    for i in range(k // 2):
        current_gain += prices[i] * (strategy[i] + 1)
    
    for i in range(k // 2, n - k // 2):
        current_gain += prices[i + k // 2] * (strategy[i + k // 2] - 1)
        max_gain = max(max_gain, current_gain)
        current_gain -= prices[i - k // 2] * (strategy[i - k // 2] + 1)
        current_gain += prices[i] * (strategy[i] + 1)
    
    return original_profit + max_gain


Solution = create_solution(max_profit_with_strategy)