# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1685
标题: Stone Game V
难度: hard
链接: https://leetcode.cn/problems/stone-game-v/
题目类型: 数组、数学、动态规划、博弈
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1563. 石子游戏 V - 几块石子 排成一行 ，每块石子都有一个关联值，关联值为整数，由数组 stoneValue 给出。 游戏中的每一轮：Alice 会将这行石子分成两个 非空行（即，左侧行和右侧行）；Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。 只 剩下一块石子 时，游戏结束。Alice 的分数最初为 0 。 返回 Alice 能够获得的最大分数 。 示例 1： 输入：stoneValue = [6,2,3,4,5,5] 输出：18 解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。 在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。 最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。 示例 2： 输入：stoneValue = [7,7,7,7,7,7,7] 输出：28 示例 3： 输入：stoneValue = [4] 输出：0 提示： * 1 <= stoneValue.length <= 500 * 1 <= stoneValue[i] <= 106
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。定义 dp[i][j] 为从 i 到 j 的子数组中 Alice 可以获得的最大分数。

算法步骤:
1. 初始化前缀和数组 prefix_sum，prefix_sum[i] 表示从 0 到 i 的元素和。
2. 初始化 dp 数组，dp[i][i] = 0，因为只有一个石子时 Alice 无法得分。
3. 从后往前遍历数组，外层循环控制子数组的长度，内层循环控制子数组的起始位置。
4. 对于每个子数组，尝试所有可能的分割点 k，计算左右两侧的和 left_sum 和 right_sum。
5. 根据 left_sum 和 right_sum 的大小关系更新 dp[i][j]。

关键点:
- 使用前缀和数组快速计算子数组的和。
- 动态规划状态转移方程：dp[i][j] = max(left_sum + dp[i][k-1], right_sum + dp[k+1][j])。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^3)，其中 n 是 stoneValue 的长度。三重循环的时间复杂度。
空间复杂度: O(n^2)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(stoneValue: List[int]) -> int:
    """
    函数式接口 - 返回 Alice 能够获得的最大分数
    """
    n = len(stoneValue)
    if n == 1:
        return 0

    # 前缀和数组
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + stoneValue[i - 1]

    # 动态规划数组
    dp = [[0] * n for _ in range(n)]

    # 从后往前遍历数组
    for length in range(2, n + 1):  # 子数组长度
        for i in range(n - length + 1):  # 子数组起始位置
            j = i + length - 1  # 子数组结束位置
            for k in range(i, j):  # 分割点
                left_sum = prefix_sum[k + 1] - prefix_sum[i]
                right_sum = prefix_sum[j + 1] - prefix_sum[k + 1]
                if left_sum < right_sum:
                    dp[i][j] = max(dp[i][j], left_sum + dp[i][k])
                elif left_sum > right_sum:
                    dp[i][j] = max(dp[i][j], right_sum + dp[k + 1][j])
                else:
                    dp[i][j] = max(dp[i][j], left_sum + max(dp[i][k], dp[k + 1][j]))

    return dp[0][n - 1]


Solution = create_solution(solution_function_name)