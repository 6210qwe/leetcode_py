# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3250
标题: Maximum Square Area by Removing Fences From a Field
难度: medium
链接: https://leetcode.cn/problems/maximum-square-area-by-removing-fences-from-a-field/
题目类型: 数组、哈希表、枚举
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2975. 移除栅栏得到的正方形田地的最大面积 - 有一个大型的 (m - 1) x (n - 1) 矩形田地，其两个对角分别是 (1, 1) 和 (m, n) ，田地内部有一些水平栅栏和垂直栅栏，分别由数组 hFences 和 vFences 给出。 水平栅栏为坐标 (hFences[i], 1) 到 (hFences[i], n)，垂直栅栏为坐标 (1, vFences[i]) 到 (m, vFences[i]) 。 返回通过 移除 一些栅栏（可能不移除）所能形成的最大面积的 正方形 田地的面积，或者如果无法形成正方形田地则返回 -1。 由于答案可能很大，所以请返回结果对 109 + 7 取余 后的值。 注意：田地外围两个水平栅栏（坐标 (1, 1) 到 (1, n) 和坐标 (m, 1) 到 (m, n) ）以及两个垂直栅栏（坐标 (1, 1) 到 (m, 1) 和坐标 (1, n) 到 (m, n) ）所包围。这些栅栏 不能 被移除。 示例 1： [https://assets.leetcode.com/uploads/2023/11/05/screenshot-from-2023-11-05-22-40-25.png] 输入：m = 4, n = 3, hFences = [2,3], vFences = [2] 输出：4 解释：移除位于 2 的水平栅栏和位于 2 的垂直栅栏将得到一个面积为 4 的正方形田地。 示例 2： [https://assets.leetcode.com/uploads/2023/11/22/maxsquareareaexample1.png] 输入：m = 6, n = 7, hFences = [2], vFences = [4] 输出：-1 解释：可以证明无法通过移除栅栏形成正方形田地。 提示： * 3 <= m, n <= 109 * 1 <= hFences.length, vFences.length <= 600 * 1 < hFences[i] < m * 1 < vFences[i] < n * hFences 和 vFences 中的元素是唯一的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用集合存储所有可能的水平和垂直间距，然后找到最大的公共间距。

算法步骤:
1. 将水平栅栏和垂直栅栏的边界加入到各自的列表中，并排序。
2. 计算所有可能的水平间距和垂直间距，并存储在集合中。
3. 找到最大公共间距，并计算其面积。
4. 如果没有找到公共间距，则返回 -1。

关键点:
- 使用集合存储间距，便于查找公共间距。
- 排序后计算间距，确保间距的有效性。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(h + v + h * log(h) + v * log(v))，其中 h 和 v 分别是水平栅栏和垂直栅栏的数量。
空间复杂度: O(h + v)，用于存储间距集合。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_square_area(m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    """
    函数式接口 - 通过移除一些栅栏（可能不移除）所能形成的最大面积的正方形田地的面积，或者如果无法形成正方形田地则返回 -1。
    """
    # 添加边界栅栏
    hFences.append(1)
    hFences.append(m)
    vFences.append(1)
    vFences.append(n)

    # 排序
    hFences.sort()
    vFences.sort()

    # 计算所有可能的水平间距
    h_diffs = set()
    for i in range(len(hFences)):
        for j in range(i + 1, len(hFences)):
            h_diffs.add(hFences[j] - hFences[i])

    # 计算所有可能的垂直间距
    v_diffs = set()
    for i in range(len(vFences)):
        for j in range(i + 1, len(vFences)):
            v_diffs.add(vFences[j] - vFences[i])

    # 找到最大公共间距
    common_diffs = h_diffs & v_diffs
    if not common_diffs:
        return -1

    max_diff = max(common_diffs)
    return (max_diff ** 2) % (10**9 + 7)


Solution = create_solution(max_square_area)