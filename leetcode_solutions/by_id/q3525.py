# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3525
标题: Maximum Energy Boost From Two Drinks
难度: medium
链接: https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/
题目类型: 数组、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3259. 超级饮料的最大强化能量 - 来自未来的体育科学家给你两个整数数组 energyDrinkA 和 energyDrinkB，数组长度都等于 n。这两个数组分别代表 A、B 两种不同能量饮料每小时所能提供的强化能量。 你需要每小时饮用一种能量饮料来 最大化 你的总强化能量。然而，如果从一种能量饮料切换到另一种，你需要等待一小时来梳理身体的能量体系（在那个小时里你将不会获得任何强化能量）。 返回在接下来的 n 小时内你能获得的 最大 总强化能量。 注意 你可以选择从饮用任意一种能量饮料开始。 示例 1： 输入：energyDrinkA = [1,3,1], energyDrinkB = [3,1,1] 输出：5 解释： 要想获得 5 点强化能量，需要选择只饮用能量饮料 A（或者只饮用 B）。 示例 2： 输入：energyDrinkA = [4,1,1], energyDrinkB = [1,1,3] 输出：7 解释： * 第一个小时饮用能量饮料 A。 * 切换到能量饮料 B ，在第二个小时无法获得强化能量。 * 第三个小时饮用能量饮料 B ，并获得强化能量。 提示： * n == energyDrinkA.length == energyDrinkB.length * 3 <= n <= 105 * 1 <= energyDrinkA[i], energyDrinkB[i] <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][0] 表示在第 i 小时结束时，最后饮用的是 A 的最大能量；dp[i][1] 表示在第 i 小时结束时，最后饮用的是 B 的最大能量。

算法步骤:
1. 初始化 dp 数组，dp[0][0] = energyDrinkA[0]，dp[0][1] = energyDrinkB[0]。
2. 从第 1 小时开始遍历，更新 dp 数组：
   - 如果当前小时饮用 A，则 dp[i][0] = max(dp[i-1][0] + energyDrinkA[i], dp[i-2][1] + energyDrinkA[i])。
   - 如果当前小时饮用 B，则 dp[i][1] = max(dp[i-1][1] + energyDrinkB[i], dp[i-2][0] + energyDrinkB[i])。
3. 最终结果是 dp[n-1][0] 和 dp[n-1][1] 中的最大值。

关键点:
- 动态规划的状态转移方程考虑了切换饮料的情况。
- 使用滚动数组优化空间复杂度。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_energy_boost(energy_drink_a: List[int], energy_drink_b: List[int]) -> int:
    """
    函数式接口 - 计算在接下来的 n 小时内你能获得的最大总强化能量
    """
    n = len(energy_drink_a)
    if n == 0:
        return 0

    # 初始化 dp 数组
    dp = [[0, 0] for _ in range(3)]
    dp[0][0] = energy_drink_a[0]
    dp[0][1] = energy_drink_b[0]

    for i in range(1, n):
        dp[i % 3][0] = max(dp[(i - 1) % 3][0] + energy_drink_a[i], dp[(i - 2) % 3][1] + energy_drink_a[i])
        dp[i % 3][1] = max(dp[(i - 1) % 3][1] + energy_drink_b[i], dp[(i - 2) % 3][0] + energy_drink_b[i])

    return max(dp[(n - 1) % 3][0], dp[(n - 1) % 3][1])


Solution = create_solution(max_energy_boost)