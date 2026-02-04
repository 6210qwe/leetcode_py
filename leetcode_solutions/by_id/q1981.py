# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1981
标题: Maximum Transaction Each Day
难度: medium
链接: https://leetcode.cn/problems/maximum-transaction-each-day/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1831. 每天的最大交易 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到每天的最大交易金额。

算法步骤:
1. 使用 GROUP BY 子句按日期分组。
2. 使用 MAX 函数找到每组中的最大交易金额。

关键点:
- 确保查询结果按日期排序。
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


def solution_function_name(transactions: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 找到每天的最大交易金额
    """
    from collections import defaultdict
    from datetime import datetime

    # 解析输入数据
    transaction_dict = defaultdict(list)
    for transaction in transactions:
        date_str, amount_str = transaction[0], transaction[1]
        date = datetime.strptime(date_str, "%Y-%m-%d")
        amount = float(amount_str)
        transaction_dict[date].append((amount, transaction))

    # 找到每天的最大交易
    result = []
    for date, trans_list in transaction_dict.items():
        max_trans = max(trans_list, key=lambda x: x[0])
        result.append(max_trans[1])

    # 按日期排序
    result.sort(key=lambda x: x[0])

    return result


Solution = create_solution(solution_function_name)