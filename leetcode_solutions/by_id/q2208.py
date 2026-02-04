# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2208
标题: Account Balance
难度: medium
链接: https://leetcode.cn/problems/account-balance/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2066. 账户余额 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个字典来记录每个账户的余额变化，并在最后计算每个账户的最终余额。

算法步骤:
1. 初始化一个字典 `balances` 来存储每个账户的余额。
2. 遍历每条交易记录，根据交易类型更新对应账户的余额。
3. 返回每个账户的最终余额。

关键点:
- 使用字典来存储和更新余额，可以高效地进行查找和更新操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是交易记录的数量。我们需要遍历每条交易记录一次。
空间复杂度: O(m)，其中 m 是账户的数量。我们需要存储每个账户的余额。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def account_balance(operations: List[List[str]]) -> int:
    """
    函数式接口 - 计算账户余额
    """
    balances = {}
    
    for operation in operations:
        op_type, account, amount = operation
        amount = int(amount)
        
        if account not in balances:
            balances[account] = 0
        
        if op_type == "Deposit":
            balances[account] += amount
        elif op_type == "Withdraw":
            balances[account] -= amount
    
    return balances.get("main", 0)


Solution = create_solution(account_balance)