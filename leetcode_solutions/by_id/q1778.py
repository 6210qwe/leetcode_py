# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1778
标题: Maximize Grid Happiness
难度: hard
链接: https://leetcode.cn/problems/maximize-grid-happiness/
题目类型: 位运算、记忆化搜索、动态规划、状态压缩
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1659. 最大化网格幸福感 - 给你四个整数 m、n、introvertsCount 和 extrovertsCount 。有一个 m x n 网格，和两种类型的人：内向的人和外向的人。总共有 introvertsCount 个内向的人和 extrovertsCount 个外向的人。 请你决定网格中应当居住多少人，并为每个人分配一个网格单元。 注意，不必 让所有人都生活在网格中。 每个人的 幸福感 计算如下： * 内向的人 开始 时有 120 个幸福感，但每存在一个邻居（内向的或外向的）他都会 失去 30 个幸福感。 * 外向的人 开始 时有 40 个幸福感，每存在一个邻居（内向的或外向的）他都会 得到 20 个幸福感。 邻居是指居住在一个人所在单元的上、下、左、右四个直接相邻的单元中的其他人。 网格幸福感 是每个人幸福感的 总和 。 返回 最大可能的网格幸福感 。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/11/15/grid_happiness.png] 输入：m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2 输出：240 解释：假设网格坐标 (row, column) 从 1 开始编号。 将内向的人放置在单元 (1,1) ，将外向的人放置在单元 (1,3) 和 (2,3) 。 - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (0 * 30)（0 位邻居）= 120 - 位于 (1,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60 - 位于 (2,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60 网格幸福感为：120 + 60 + 60 = 240 上图展示该示例对应网格中每个人的幸福感。内向的人在浅绿色单元中，而外向的人在浅紫色单元中。 示例 2： 输入：m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1 输出：260 解释：将内向的人放置在单元 (1,1) 和 (3,1) ，将外向的人放置在单元 (2,1) 。 - 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90 - 位于 (2,1) 的外向的人的幸福感：40（初始幸福感）+ (2 * 20)（2 位邻居）= 80 - 位于 (3,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90 网格幸福感为 90 + 80 + 90 = 260 示例 3： 输入：m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0 输出：240 提示： * 1 <= m, n <= 5 * 0 <= introvertsCount, extrovertsCount <= min(m * n, 6)
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和状态压缩来解决这个问题。我们使用一个三维数组 dp 来记录每个状态的最大幸福感。状态由当前行的状态、剩余内向人数和剩余外向人数组成。

算法步骤:
1. 初始化 dp 数组，dp[i][j][k] 表示前 i 行，剩余 j 个内向人，剩余 k 个外向人的最大幸福感。
2. 定义一个函数 `get_happiness` 来计算给定两行状态之间的幸福感变化。
3. 使用递归和记忆化搜索来填充 dp 数组。
4. 返回 dp 数组的最终结果。

关键点:
- 使用状态压缩来表示每一行的状态。
- 使用递归和记忆化搜索来优化动态规划过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(3^N * N * M * I * E)，其中 N 是列数，M 是行数，I 是内向人数，E 是外向人数。
空间复杂度: O(3^N * I * E)，用于存储 dp 数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from functools import lru_cache

def get_happiness(state1: int, state2: int) -> int:
    happiness = 0
    for i in range(3):
        if state1 & (1 << i):
            if state2 & (1 << i):
                happiness += 60
            else:
                happiness -= 30
        elif state2 & (1 << i):
            happiness += 40
    return happiness

@lru_cache(None)
def dfs(row: int, state: int, intro_count: int, extro_count: int) -> int:
    if row == m or (intro_count == 0 and extro_count == 0):
        return 0
    
    max_happiness = dfs(row + 1, 0, intro_count, extro_count)
    
    for next_state in range(3 ** n):
        next_intro_count = intro_count
        next_extro_count = extro_count
        current_happiness = 0
        
        for i in range(n):
            if next_state & (1 << i):
                if (next_state >> i) & 1:
                    next_intro_count -= 1
                    current_happiness += 120
                else:
                    next_extro_count -= 1
                    current_happiness += 40
        
        if next_intro_count >= 0 and next_extro_count >= 0:
            current_happiness += get_happiness(state, next_state)
            max_happiness = max(max_happiness, current_happiness + dfs(row + 1, next_state, next_intro_count, next_extro_count))
    
    return max_happiness

def solution_function_name(m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
    """
    函数式接口 - 使用动态规划和状态压缩来最大化网格幸福感
    """
    global m, n
    m, n = m, n
    return dfs(0, 0, introvertsCount, extrovertsCount)

Solution = create_solution(solution_function_name)