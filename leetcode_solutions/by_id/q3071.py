# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3071
标题: Drop Duplicate Rows
难度: easy
链接: https://leetcode.cn/problems/drop-duplicate-rows/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2882. 删去重复的行 - DataFrame customers +-------------+--------+ | Column Name | Type | +-------------+--------+ | customer_id | int | | name | object | | email | object | +-------------+--------+ 在 DataFrame 中基于 email 列存在一些重复行。 编写一个解决方案，删除这些重复行，仅保留第一次出现的行。 返回结果格式如下例所示。 示例 1: 输入： +-------------+---------+---------------------+ | customer_id | name | email | +-------------+---------+---------------------+ | 1 | Ella | emily@example.com | | 2 | David | michael@example.com | | 3 | Zachary | sarah@example.com | | 4 | Alice | john@example.com | | 5 | Finn | john@example.com | | 6 | Violet | alice@example.com | +-------------+---------+---------------------+ 输出： +-------------+---------+---------------------+ | customer_id | name | email | +-------------+---------+---------------------+ | 1 | Ella | emily@example.com | | 2 | David | michael@example.com | | 3 | Zachary | sarah@example.com | | 4 | Alice | john@example.com | | 6 | Violet | alice@example.com | +-------------+---------+---------------------+ 解释： Alice (customer_id = 4) 和 Finn (customer_id = 5) 都使用 john@example.com，因此只保留该邮箱地址的第一次出现。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
