# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1658
标题: Minimum Swaps to Arrange a Binary Grid
难度: medium
链接: https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/
题目类型: 贪心、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1536. 排布二进制网格的最少交换次数 - 给你一个 n x n 的二进制网格 grid，每一次操作中，你可以选择网格的 相邻两行 进行交换。 一个符合要求的网格需要满足主对角线以上的格子全部都是 0 。 请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 -1 。 主对角线指的是从 (1, 1) 到 (n, n) 的这些格子。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/02/fw.jpg] 输入：grid = [[0,0,1],[1,1,0],[1,0,0]] 输出：3 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/02/e2.jpg] 输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]] 输出：-1 解释：所有行都是一样的，交换相邻行无法使网格符合要求。 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/08/02/e3.jpg] 输入：grid = [[1,0,0],[1,1,0],[1,1,1]] 输出：0 提示： * n == grid.length * n == grid[i].length * 1 <= n <= 200 * grid[i][j] 要么是 0 要么是 1 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用贪心算法，通过计算每行从右到左第一个1的位置，并进行排序，然后通过冒泡排序的思想进行交换。

算法步骤:
1. 计算每行从右到左第一个1的位置，并存储在数组中。
2. 检查是否可以满足条件，如果不能则返回-1。
3. 通过冒泡排序的思想进行交换，记录交换次数。

关键点:
- 通过计算每行从右到左第一个1的位置，可以确定每行需要移动到的目标位置。
- 使用冒泡排序的思想进行交换，确保每行都能移动到正确的位置。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是网格的大小。最坏情况下，我们需要进行 n^2 次交换。
空间复杂度: O(n)，用于存储每行从右到左第一个1的位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_swaps(grid: List[List[int]]) -> int:
    """
    函数式接口 - 计算使网格满足要求的最少交换次数
    """
    n = len(grid)
    # 计算每行从右到左第一个1的位置
    trailing_zeros = []
    for row in grid:
        count = 0
        for i in range(n - 1, -1, -1):
            if row[i] == 0:
                count += 1
            else:
                break
        trailing_zeros.append(count)

    # 检查是否可以满足条件
    for i in range(n):
        if trailing_zeros[i] < n - i - 1:
            return -1

    # 通过冒泡排序的思想进行交换
    swaps = 0
    for i in range(n):
        for j in range(i + 1, n):
            if trailing_zeros[j] < n - i - 1:
                trailing_zeros[i], trailing_zeros[j] = trailing_zeros[j], trailing_zeros[i]
                swaps += 1

    return swaps


Solution = create_solution(min_swaps)