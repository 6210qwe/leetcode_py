# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 533
标题: Lonely Pixel II
难度: medium
链接: https://leetcode.cn/problems/lonely-pixel-ii/
题目类型: 数组、哈希表、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
533. 孤独像素 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个哈希表分别记录每一行和每一列中 'B' 的数量。然后遍历矩阵，找到满足条件的 'B'。

算法步骤:
1. 初始化两个哈希表 `row_count` 和 `col_count`，分别记录每一行和每一列中 'B' 的数量。
2. 遍历矩阵，更新 `row_count` 和 `col_count`。
3. 再次遍历矩阵，检查每个 'B' 是否是唯一的，即其所在行和列中 'B' 的数量都为 1。

关键点:
- 使用哈希表来高效统计每一行和每一列中 'B' 的数量。
- 两次遍历矩阵，一次用于统计，一次用于检查。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)，其中 m 是矩阵的行数，n 是矩阵的列数。
空间复杂度: O(m + n)，用于存储每一行和每一列中 'B' 的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_lonely_pixel(picture: List[List[str]]) -> int:
    """
    函数式接口 - 寻找孤独像素 II
    """
    if not picture or not picture[0]:
        return 0

    m, n = len(picture), len(picture[0])
    row_count = [0] * m
    col_count = [0] * n

    # 统计每一行和每一列中 'B' 的数量
    for i in range(m):
        for j in range(n):
            if picture[i][j] == 'B':
                row_count[i] += 1
                col_count[j] += 1

    lonely_count = 0

    # 检查每个 'B' 是否是唯一的
    for i in range(m):
        for j in range(n):
            if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                lonely_count += 1

    return lonely_count


Solution = create_solution(find_lonely_pixel)