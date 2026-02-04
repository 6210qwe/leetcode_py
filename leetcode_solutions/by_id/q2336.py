# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2336
标题: The Number of Users That Are Eligible for Discount
难度: easy
链接: https://leetcode.cn/problems/the-number-of-users-that-are-eligible-for-discount/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2205. 有资格享受折扣的用户数量 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选出符合条件的用户数量

算法步骤:
1. 从 `Purchases` 表中选择所有记录。
2. 使用 `GROUP BY` 子句按 `user_id` 分组，并计算每个用户的购买次数。
3. 使用 `HAVING` 子句筛选出购买次数大于等于 2 的用户。
4. 计算这些用户的数量。

关键点:
- 使用 `GROUP BY` 和 `HAVING` 子句来筛选符合条件的用户。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是 `Purchases` 表中的记录数。需要遍历整个表进行分组和计数。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(purchases: List[List[str]]) -> int:
    """
    函数式接口 - 实现最优解法
    """
    from collections import defaultdict

    # 统计每个用户的购买次数
    user_purchases = defaultdict(int)
    for purchase in purchases:
        user_id = purchase[1]
        user_purchases[user_id] += 1

    # 筛选出购买次数大于等于 2 的用户数量
    eligible_users_count = sum(1 for count in user_purchases.values() if count >= 2)

    return eligible_users_count


Solution = create_solution(solution_function_name)