# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1555
标题: Number of Ways of Cutting a Pizza
难度: hard
链接: https://leetcode.cn/problems/number-of-ways-of-cutting-a-pizza/
题目类型: 记忆化搜索、数组、动态规划、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1444. 切披萨的方案数 - 给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1 次，得到 k 块披萨并送给别人。 切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。 请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/10/ways_to_cut_apple_1.png] 输入：pizza = ["A..","AAA","..."], k = 3 输出：3 解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。 示例 2： 输入：pizza = ["A..","AA.","..."], k = 3 输出：1 示例 3： 输入：pizza = ["A..","A..","..."], k = 1 输出：1 提示： * 1 <= rows, cols <= 50 * rows == pizza.length * cols == pizza[i].length * 1 <= k <= 10 * pizza 只包含字符 'A' 和 '.' 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用动态规划和记忆化搜索来解决这个问题。我们使用一个三维数组 dp[r][c][k] 来表示从 (r, c) 开始切 k 次的方案数。

算法步骤:
1. 初始化前缀和数组 pre_sum，用于快速计算某个子矩形中苹果的数量。
2. 定义递归函数 dfs(r, c, k)，表示从 (r, c) 开始切 k 次的方案数。
3. 在递归函数中，首先检查当前子矩形是否有苹果，如果没有则返回 0。
4. 如果 k 为 0，说明不需要再切了，直接返回 1。
5. 否则，遍历所有可能的切割位置，分别尝试水平和垂直切割，并累加结果。
6. 使用记忆化搜索来避免重复计算。

关键点:
- 使用前缀和数组快速计算子矩形中的苹果数量。
- 使用记忆化搜索优化递归过程。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(rows * cols * k * (rows + cols))，其中 rows 和 cols 分别是披萨的行数和列数，k 是切割次数。
空间复杂度: O(rows * cols * k)，用于存储记忆化搜索的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

MOD = 10**9 + 7

def ways(pizza: List[str], k: int) -> int:
    rows, cols = len(pizza), len(pizza[0])
    
    # 前缀和数组
    pre_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            pre_sum[r][c] = pre_sum[r-1][c] + pre_sum[r][c-1] - pre_sum[r-1][c-1] + (pizza[r-1][c-1] == 'A')
    
    # 检查子矩形是否有苹果
    def has_apple(r1, c1, r2, c2):
        return pre_sum[r2+1][c2+1] - pre_sum[r1][c2+1] - pre_sum[r2+1][c1] + pre_sum[r1][c1] > 0
    
    # 记忆化搜索
    from functools import lru_cache
    @lru_cache(None)
    def dfs(r, c, k):
        if k == 0:
            return 1
        ways = 0
        # 水平切割
        for nr in range(r + 1, rows):
            if has_apple(r, c, nr - 1, cols - 1) and has_apple(nr, c, rows - 1, cols - 1):
                ways = (ways + dfs(nr, c, k - 1)) % MOD
        # 垂直切割
        for nc in range(c + 1, cols):
            if has_apple(r, c, rows - 1, nc - 1) and has_apple(r, nc, rows - 1, cols - 1):
                ways = (ways + dfs(r, nc, k - 1)) % MOD
        return ways
    
    return dfs(0, 0, k - 1)

Solution = create_solution(ways)