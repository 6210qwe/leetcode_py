# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1494
标题: Activity Participants
难度: medium
链接: https://leetcode.cn/problems/activity-participants/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1355. 活动参与者 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个活动的参与者数量。

算法步骤:
1. 使用 GROUP BY 子句按 activity 字段分组。
2. 使用 COUNT 函数计算每组的参与者数量。
3. 使用 ORDER BY 子句按参与者数量降序排列。

关键点:
- 使用 GROUP BY 和 COUNT 函数进行分组和计数。
- 使用 ORDER BY 子句对结果进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是表中记录的数量。GROUP BY 和 COUNT 操作的时间复杂度为 O(n)，ORDER BY 操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，查询操作的空间复杂度主要取决于数据库的实现，但通常不会超过常数级别。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name():
    """
    函数式接口 - 返回 SQL 查询语句
    """
    # 实现最优解法
    query = """
    SELECT activity, COUNT(*) AS count
    FROM Friends
    GROUP BY activity
    ORDER BY count DESC
    """
    return query


Solution = create_solution(solution_function_name)