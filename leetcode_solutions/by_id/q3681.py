# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3681
标题: Maximum Area Rectangle With Point Constraints I
难度: medium
链接: https://leetcode.cn/problems/maximum-area-rectangle-with-point-constraints-i/
题目类型: 树状数组、线段树、几何、数组、数学、枚举、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3380. 用点构造面积最大的矩形 I - 给你一个数组 points，其中 points[i] = [xi, yi] 表示无限平面上一点的坐标。 你的任务是找出满足以下条件的矩形可能的 最大 面积： * 矩形的四个顶点必须是数组中的 四个 点。 * 矩形的内部或边界上 不能 包含任何其他点。 * 矩形的边与坐标轴 平行 。 返回可以获得的 最大面积 ，如果无法形成这样的矩形，则返回 -1。 示例 1： 输入： points = [[1,1],[1,3],[3,1],[3,3]] 输出：4 解释： 示例 1 图示 [https://assets.leetcode.com/uploads/2024/11/02/example1.png] 我们可以用这 4 个点作为顶点构成一个矩形，并且矩形内部或边界上没有其他点。因此，最大面积为 4 。 示例 2： 输入： points = [[1,1],[1,3],[3,1],[3,3],[2,2]] 输出：-1 解释： 示例 2 图示 [https://assets.leetcode.com/uploads/2024/11/02/example2.png] 唯一一组可能构成矩形的点为 [1,1], [1,3], [3,1] 和 [3,3]，但点 [2,2] 总是位于矩形内部。因此，返回 -1 。 示例 3： 输入： points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]] 输出：2 解释： 示例 3 图示 [https://assets.leetcode.com/uploads/2024/11/02/example3.png] 点 [1,3], [1,2], [3,2], [3,3] 可以构成面积最大的矩形，面积为 2。此外，点 [1,1], [1,2], [3,1], [3,2] 也可以构成一个符合题目要求的矩形，面积相同。 提示： * 1 <= points.length <= 10 * points[i].length == 2 * 0 <= xi, yi <= 100 * 给定的所有点都是 唯一 的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过枚举所有可能的矩形，检查每个矩形是否符合条件。

算法步骤:
1. 将所有点按 x 坐标和 y 坐标分别排序。
2. 枚举所有可能的矩形，检查矩形内部或边界上是否有其他点。
3. 计算符合条件的矩形的最大面积。

关键点:
- 使用集合来快速检查点的存在性。
- 通过排序和枚举来减少不必要的计算。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2 log n)，其中 n 是 points 的长度。排序操作的时间复杂度为 O(n log n)，枚举矩形的时间复杂度为 O(n^2)。
空间复杂度: O(n)，用于存储点的集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(points: List[List[int]]) -> int:
    """
    函数式接口 - 找出满足条件的最大面积矩形
    """
    if len(points) < 4:
        return -1

    # 将点按 x 坐标和 y 坐标分别排序
    points.sort(key=lambda p: (p[0], p[1]))
    point_set = set(tuple(p) for p in points)

    max_area = -1

    # 枚举所有可能的矩形
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # 检查矩形的对角线是否存在
            if (x1, y2) in point_set and (x2, y1) in point_set:
                # 检查矩形内部或边界上是否有其他点
                if all((x, y) not in point_set for x in range(x1 + 1, x2) for y in range(min(y1, y2), max(y1, y2) + 1)):
                    area = abs(x2 - x1) * abs(y2 - y1)
                    max_area = max(max_area, area)

    return max_area


Solution = create_solution(solution_function_name)