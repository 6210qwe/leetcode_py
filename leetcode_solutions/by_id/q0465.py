# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 465
标题: Optimal Account Balancing
难度: hard
链接: https://leetcode.cn/problems/optimal-account-balancing/
题目类型: 位运算、数组、动态规划、回溯、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
465. 最优账单平衡 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯算法，最小化转账次数

算法步骤:
1. 计算每个人的净余额（借入-借出）
2. 只保留非零余额的人
3. 使用回溯，尝试所有可能的配对方式
4. 找到最小转账次数

关键点:
- 回溯+剪枝
- 时间复杂度O(n!)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n!) - 最坏情况需要尝试所有配对
空间复杂度: O(n) - 存储余额数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def optimal_account_balancing(transactions: List[List[int]]) -> int:
    """
    函数式接口 - 最优账单平衡
    
    实现思路:
    计算每个人的净余额，使用回溯算法找到最小转账次数。
    
    Args:
        transactions: 交易列表，每个交易为[from, to, amount]
        
    Returns:
        最小转账次数
        
    Example:
        >>> optimal_account_balancing([[0,1,10],[2,0,5]])
        2
    """
    # 计算每个人的净余额
    balance = defaultdict(int)
    for from_person, to_person, amount in transactions:
        balance[from_person] -= amount
        balance[to_person] += amount
    
    # 只保留非零余额
    debts = [amount for amount in balance.values() if amount != 0]
    
    def backtrack(start: int) -> int:
        """回溯函数"""
        # 跳过已处理的债务
        while start < len(debts) and debts[start] == 0:
            start += 1
        
        if start == len(debts):
            return 0
        
        min_transfers = float('inf')
        for i in range(start + 1, len(debts)):
            # 如果两个债务符号相反，可以配对
            if debts[start] * debts[i] < 0:
                debts[i] += debts[start]
                min_transfers = min(min_transfers, 1 + backtrack(start + 1))
                debts[i] -= debts[start]
        
        return min_transfers
    
    return backtrack(0)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(optimal_account_balancing)
