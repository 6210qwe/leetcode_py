# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2311
标题: Minimum White Tiles After Covering With Carpets
难度: hard
链接: https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/
题目类型: 字符串、动态规划、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2209. 用地毯覆盖后的最少白色砖块 - 给你一个下标从 0 开始的 二进制 字符串 floor ，它表示地板上砖块的颜色。 * floor[i] = '0' 表示地板上第 i 块砖块的颜色是 黑色 。 * floor[i] = '1' 表示地板上第 i 块砖块的颜色是 白色 。 同时给你 numCarpets 和 carpetLen 。你有 numCarpets 条 黑色 的地毯，每一条 黑色 的地毯长度都为 carpetLen 块砖块。请你使用这些地毯去覆盖砖块，使得未被覆盖的剩余 白色 砖块的数目 最小 。地毯相互之间可以覆盖。 请你返回没被覆盖的白色砖块的 最少 数目。 示例 1： [https://assets.leetcode.com/uploads/2022/02/10/ex1-1.png] 输入：floor = "10110101", numCarpets = 2, carpetLen = 2 输出：2 解释： 上图展示了剩余 2 块白色砖块的方案。 没有其他方案可以使未被覆盖的白色砖块少于 2 块。 示例 2： [https://assets.leetcode.com/uploads/2022/02/10/ex2.png] 输入：floor = "11111", numCarpets = 2, carpetLen = 3 输出：0 解释： 上图展示了所有白色砖块都被覆盖的一种方案。 注意，地毯相互之间可以覆盖。 提示： * 1 <= carpetLen <= floor.length <= 1000 * floor[i] 要么是 '0' ，要么是 '1' 。 * 1 <= numCarpets <= 1000
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划来解决这个问题。我们定义 dp[i][j] 表示使用 j 条地毯覆盖前 i 个砖块后，剩余的最少白色砖块数。

算法步骤:
1. 初始化一个二维数组 dp，其中 dp[i][j] 表示使用 j 条地毯覆盖前 i 个砖块后，剩余的最少白色砖块数。
2. 遍历每个砖块 i 和地毯数量 j，更新 dp[i][j]。
3. 如果当前砖块是黑色的，那么 dp[i][j] = dp[i-1][j]。
4. 如果当前砖块是白色的，那么有两种选择：
   - 不使用地毯覆盖当前砖块，dp[i][j] = dp[i-1][j] + 1。
   - 使用一条地毯覆盖当前砖块及其前面的 carpetLen-1 个砖块，dp[i][j] = dp[max(0, i-carpetLen)][j-1]。
5. 返回 dp[n][numCarpets]，即使用 numCarpets 条地毯覆盖 n 个砖块后，剩余的最少白色砖块数。

关键点:
- 使用动态规划来优化时间和空间复杂度。
- 通过前缀和来快速计算覆盖的白色砖块数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * numCarpets)，其中 n 是 floor 的长度。
空间复杂度: O(n * numCarpets)，用于存储动态规划数组。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minimum_white_tiles(floor: str, num_carpets: int, carpet_len: int) -> int:
    n = len(floor)
    dp = [[float('inf')] * (num_carpets + 1) for _ in range(n + 1)]
    
    # 初始化 dp 数组
    for j in range(num_carpets + 1):
        dp[0][j] = 0
    
    for i in range(1, n + 1):
        for j in range(num_carpets + 1):
            if floor[i - 1] == '0':
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + 1
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[max(0, i - carpet_len)][j - 1])
    
    return dp[n][num_carpets]


Solution = create_solution(minimum_white_tiles)