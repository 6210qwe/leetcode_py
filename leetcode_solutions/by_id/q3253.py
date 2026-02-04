# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3253
标题: Symmetric Coordinates
难度: medium
链接: https://leetcode.cn/problems/symmetric-coordinates/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2978. 对称坐标 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到所有对称的坐标点。

算法步骤:
1. 创建一个临时表来存储输入的坐标点。
2. 使用自连接查询来找到所有对称的坐标点。
3. 返回结果集。

关键点:
- 使用自连接查询来找到对称的坐标点。
- 确保查询的时间复杂度和空间复杂度最优。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是坐标点的数量。因为我们需要进行自连接查询。
空间复杂度: O(n)，因为我们需要存储输入的坐标点。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(points: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 找到所有对称的坐标点
    """
    # 创建一个临时表来存储输入的坐标点
    temp_table = {}
    for x, y in points:
        if (y, x) in temp_table:
            temp_table[(y, x)].append([x, y])
        else:
            temp_table[(y, x)] = [[x, y]]

    # 收集所有对称的坐标点
    symmetric_points = []
    for key, value in temp_table.items():
        if len(value) > 1:
            symmetric_points.extend(value)

    return symmetric_points


Solution = create_solution(solution_function_name)