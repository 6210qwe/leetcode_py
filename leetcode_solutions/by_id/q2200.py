# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2200
标题: Stamping the Grid
难度: hard
链接: https://leetcode.cn/problems/stamping-the-grid/
题目类型: 贪心、数组、矩阵、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2132. 用邮票贴满网格图 - 给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。 给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ： 1. 覆盖所有 空 格子。 2. 不覆盖任何 被占据 的格子。 3. 我们可以放入任意数目的邮票。 4. 邮票可以相互有 重叠 部分。 5. 邮票不允许 旋转 。 6. 邮票必须完全在矩阵 内 。 如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。 示例 1： [https://assets.leetcode.com/uploads/2021/11/03/ex1.png] 输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3 输出：true 解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。 示例 2： [https://assets.leetcode.com/uploads/2021/11/03/ex2.png] 输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 输出：false 解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。 提示： * m == grid.length * n == grid[r].length * 1 <= m, n <= 105 * 1 <= m * n <= 2 * 105 * grid[r][c] 要么是 0 ，要么是 1 。 * 1 <= stampHeight, stampWidth <= 105
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用二维前缀和来快速计算子矩阵的和，并使用贪心算法来放置邮票。

算法步骤:
1. 计算二维前缀和数组。
2. 初始化一个二维数组 `covered` 来记录每个位置是否被邮票覆盖。
3. 遍历每个可能的邮票左上角位置，检查该位置是否可以放置邮票。
4. 如果可以放置邮票，则更新 `covered` 数组。
5. 最后检查 `covered` 数组，确保所有空格子都被覆盖。

关键点:
- 使用二维前缀和快速计算子矩阵的和。
- 使用贪心算法从左上到右下依次尝试放置邮票。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m * n)
空间复杂度: O(m * n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List

def can_stamp(grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
    m, n = len(grid), len(grid[0])
    
    # 计算二维前缀和数组
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_sum[i][j] = grid[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
    
    # 初始化 covered 数组
    covered = [[False] * n for _ in range(m)]
    
    # 检查每个可能的邮票左上角位置
    for i in range(m - stampHeight + 1):
        for j in range(n - stampWidth + 1):
            if prefix_sum[i + stampHeight][j + stampWidth] - prefix_sum[i + stampHeight][j] - prefix_sum[i][j + stampWidth] + prefix_sum[i][j] == 0:
                for r in range(i, i + stampHeight):
                    for c in range(j, j + stampWidth):
                        covered[r][c] = True
    
    # 检查所有空格子是否被覆盖
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and not covered[i][j]:
                return False
    
    return True

Solution = create_solution(can_stamp)