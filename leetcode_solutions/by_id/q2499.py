# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2499
标题: Minimum Money Required Before Transactions
难度: hard
链接: https://leetcode.cn/problems/minimum-money-required-before-transactions/
题目类型: 贪心、数组、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2412. 完成所有交易的初始最少钱数 - 给你一个下标从 0 开始的二维整数数组 transactions，其中transactions[i] = [costi, cashbacki] 。 数组描述了若干笔交易。其中每笔交易必须以 某种顺序 恰好完成一次。在任意一个时刻，你有一定数目的钱 money ，为了完成交易 i ，money >= costi 这个条件必须为真。执行交易后，你的钱数 money 变成 money - costi + cashbacki 。 请你返回 任意一种 交易顺序下，你都能完成所有交易的最少钱数 money 是多少。 示例 1： 输入：transactions = [[2,1],[5,0],[4,2]] 输出：10 解释： 刚开始 money = 10 ，交易可以以任意顺序进行。 可以证明如果 money < 10 ，那么某些交易无法进行。 示例 2： 输入：transactions = [[3,0],[0,3]] 输出：3 解释： - 如果交易执行的顺序是 [[3,0],[0,3]] ，完成所有交易需要的最少钱数是 3 。 - 如果交易执行的顺序是 [[0,3],[3,0]] ，完成所有交易需要的最少钱数是 0 。 所以，刚开始钱数为 3 ，任意顺序下交易都可以全部完成。 提示： * 1 <= transactions.length <= 105 * transactions[i].length == 2 * 0 <= costi, cashbacki <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，将交易分为两类：成本大于或等于回扣的交易和成本小于回扣的交易。对于成本大于或等于回扣的交易，我们按成本降序排序；对于成本小于回扣的交易，我们按回扣升序排序。然后计算完成所有交易所需的最少初始资金。

算法步骤:
1. 将交易分为两类：成本大于或等于回扣的交易和成本小于回扣的交易。
2. 对于成本大于或等于回扣的交易，按成本降序排序。
3. 对于成本小于回扣的交易，按回扣升序排序。
4. 计算完成所有交易所需的最少初始资金。

关键点:
- 通过分类和排序，确保在任意顺序下都能完成所有交易。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 transactions 的长度，因为排序操作的时间复杂度是 O(n log n)。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def min_money_required(transactions: List[List[int]]) -> int:
    """
    函数式接口 - 返回完成所有交易所需的最少初始资金
    """
    # 分类交易
    high_cost_transactions = []
    low_cost_transactions = []
    
    for cost, cashback in transactions:
        if cost >= cashback:
            high_cost_transactions.append((cost, cashback))
        else:
            low_cost_transactions.append((cost, cashback))
    
    # 排序
    high_cost_transactions.sort(key=lambda x: -x[0])
    low_cost_transactions.sort(key=lambda x: x[1])
    
    # 计算最少初始资金
    max_cost = 0
    current_money = 0
    
    for cost, cashback in high_cost_transactions + low_cost_transactions:
        if current_money < cost:
            max_cost = max(max_cost, cost - current_money)
        current_money += cashback - cost
    
    return max_cost

Solution = create_solution(min_money_required)