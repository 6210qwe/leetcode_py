# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2769
标题: Array of Objects to Matrix
难度: hard
链接: https://leetcode.cn/problems/array-of-objects-to-matrix/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2675. 将对象数组转换为矩阵 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个键的值，并按行和列填充结果矩阵。

算法步骤:
1. 初始化一个哈希表 `key_to_values` 来存储每个键对应的值列表。
2. 遍历输入的对象数组 `objects`，将每个对象的键值对存入哈希表中。
3. 确定矩阵的行数和列数。
4. 初始化结果矩阵 `matrix`，并按行和列填充矩阵。
5. 返回结果矩阵。

关键点:
- 使用哈希表来存储每个键的值列表，便于后续快速查找。
- 矩阵的行数是所有键的最大长度，列数是对象数组的长度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是对象数组的长度，m 是每个对象的键的最大数量。
空间复杂度: O(n * m)，用于存储哈希表和结果矩阵。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(objects: List[dict], rowHeaders: List[str], colHeaders: List[str]) -> List[List[Optional[str]]]:
    """
    函数式接口 - 将对象数组转换为矩阵
    """
    # 初始化哈希表来存储每个键的值列表
    key_to_values = {key: [] for key in rowHeaders}
    
    # 遍历输入的对象数组，将每个对象的键值对存入哈希表中
    for obj in objects:
        for key in rowHeaders:
            key_to_values[key].append(obj.get(key))
    
    # 初始化结果矩阵
    matrix = []
    for key in rowHeaders:
        matrix.append(key_to_values[key])
    
    return matrix


Solution = create_solution(solution_function_name)