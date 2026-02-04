# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1374
标题: Leftmost Column with at Least a One
难度: medium
链接: https://leetcode.cn/problems/leftmost-column-with-at-least-a-one/
题目类型: 数组、二分查找、交互、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1428. 至少有一个 1 的最左端列 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二分查找来找到至少有一个 1 的最左端列。

算法步骤:
1. 初始化左右边界，left 为 0，right 为矩阵的列数减一。
2. 在 left 小于等于 right 的情况下，进行以下操作：
   - 计算中间列 mid。
   - 检查当前行中从第 mid 列开始是否有 1，如果有，则将 right 更新为 mid - 1。
   - 如果没有，则将 left 更新为 mid + 1。
3. 最后返回 left，如果 left 等于列数，则说明没有找到 1，返回 -1。

关键点:
- 使用二分查找来减少查找的时间复杂度。
- 通过检查当前行中从中间列开始是否有 1 来调整左右边界。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m log n)，其中 m 是行数，n 是列数。每次二分查找的时间复杂度是 O(log n)，最多进行 m 次。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class BinaryMatrix:
    def get(self, row: int, col: int) -> int:
        # 假设这是一个预定义的接口，用于获取矩阵中的元素
        pass

    def dimensions(self) -> List[int]:
        # 假设这是一个预定义的接口，用于获取矩阵的维度
        pass


def solution_function_name(binaryMatrix: BinaryMatrix) -> int:
    """
    函数式接口 - 找到至少有一个 1 的最左端列
    """
    rows, cols = binaryMatrix.dimensions()
    left, right = 0, cols - 1
    while left <= right:
        mid = (left + right) // 2
        if any(binaryMatrix.get(row, mid) == 1 for row in range(rows)):
            right = mid - 1
        else:
            left = mid + 1
    return left if left < cols else -1


Solution = create_solution(solution_function_name)