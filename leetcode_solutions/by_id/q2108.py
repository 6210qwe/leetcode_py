# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2108
标题: Minimize the Difference Between Target and Chosen Elements
难度: medium
链接: https://leetcode.cn/problems/minimize-the-difference-between-target-and-chosen-elements/
题目类型: 数组、动态规划、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1981. 最小化目标值与所选元素的差 - 给你一个大小为 m x n 的整数矩阵 mat 和一个整数 target 。 从矩阵的 每一行 中选择一个整数，你的目标是 最小化 所有选中元素之 和 与目标值 target 的 绝对差 。 返回 最小的绝对差 。 a 和 b 两数字的 绝对差 是 a - b 的绝对值。 示例 1： [https://assets.leetcode.com/uploads/2021/08/03/matrix1.png] 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13 输出：0 解释：一种可能的最优选择方案是： - 第一行选出 1 - 第二行选出 5 - 第三行选出 7 所选元素的和是 13 ，等于目标值，所以绝对差是 0 。 示例 2： [https://assets.leetcode.com/uploads/2021/08/03/matrix1-1.png] 输入：mat = [[1],[2],[3]], target = 100 输出：94 解释：唯一一种选择方案是： - 第一行选出 1 - 第二行选出 2 - 第三行选出 3 所选元素的和是 6 ，绝对差是 94 。 示例 3： [https://assets.leetcode.com/uploads/2021/08/03/matrix1-3.png] 输入：mat = [[1,2,9,8,7]], target = 6 输出：1 解释：最优的选择方案是选出第一行的 7 。 绝对差是 1 。 提示： * m == mat.length * n == mat[i].length * 1 <= m, n <= 70 * 1 <= mat[i][j] <= 70 * 1 <= target <= 800
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们使用一个集合来存储每一步可能的和，并在每一步更新这个集合。

算法步骤:
1. 初始化一个集合 `dp`，包含初始值 0。
2. 遍历每一行，对于每个元素，计算当前行所有可能的和，并将这些和存储在一个新的集合 `new_dp` 中。
3. 更新 `dp` 为 `new_dp`。
4. 在遍历完所有行后，找到 `dp` 中最接近 `target` 的值，并返回其与 `target` 的绝对差。

关键点:
- 使用集合来存储每一步可能的和，避免重复计算。
- 通过动态规划逐步更新可能的和，确保每一步都只保留必要的和。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n * min(n, target))
空间复杂度: O(min(n, target))
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimizeTheDifference(mat: List[List[int]], target: int) -> int:
    """
    函数式接口 - 实现最优解法
    """
    m, n = len(mat), len(mat[0])
    
    # 初始化 dp 集合
    dp = {0}
    
    for row in mat:
        new_dp = set()
        for prev_sum in dp:
            for num in row:
                new_sum = prev_sum + num
                if new_sum < target or (not new_dp or new_sum < max(new_dp)):
                    new_dp.add(new_sum)
        dp = new_dp
    
    # 找到最接近 target 的和
    return min(abs(s - target) for s in dp)


Solution = create_solution(minimizeTheDifference)