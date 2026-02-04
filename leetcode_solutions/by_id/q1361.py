# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1361
标题: Tiling a Rectangle with the Fewest Squares
难度: hard
链接: https://leetcode.cn/problems/tiling-a-rectangle-with-the-fewest-squares/
题目类型: 回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1240. 铺瓷砖 - 给定一个大小为 n x m 的长方形，返回贴满矩形所需的整数边正方形的最小数量。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/10/25/sample_11_1592.png] 输入：n = 2, m = 3 输出：3 解释：需要 3 个正方形来覆盖长方形。 2 个 1x1 的正方形 1 个 2x2 的正方形 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/10/25/sample_22_1592.png] 输入：n = 5, m = 8 输出：5 示例 3： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2019/10/25/sample_33_1592.png] 输入：n = 11, m = 13 输出：6 提示： * 1 <= n, m <= 13
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用回溯法尝试所有可能的正方形铺法，找到最少的正方形数量。

算法步骤:
1. 初始化一个二维数组表示矩形，并记录当前最小正方形数量。
2. 从左上角开始，找到第一个未被覆盖的位置。
3. 尝试在此位置放置不同大小的正方形，递归地继续填充剩余部分。
4. 如果当前正方形数量小于已记录的最小值，则更新最小值。
5. 回溯并尝试其他可能的正方形放置方式。

关键点:
- 使用递归和回溯来尝试所有可能的正方形铺法。
- 通过剪枝减少不必要的计算，例如当当前正方形数量已经大于已记录的最小值时，提前终止递归。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^(n*m)) - 最坏情况下需要尝试所有可能的正方形铺法。
空间复杂度: O(n*m) - 递归调用栈和存储矩形状态的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def tiling_rectangle(n: int, m: int) -> int:
    def backtrack(grid, min_squares):
        if all(cell == 1 for row in grid for cell in row):
            return 0
        
        min_squares[0] = float('inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    start_i, start_j = i, j
                    break
            else:
                continue
            break
        
        for size in range(min(n - start_i, m - start_j), 0, -1):
            if any(grid[start_i + k][start_j + k] == 1 for k in range(size)):
                break
            
            # Place square
            for k in range(size):
                for l in range(size):
                    grid[start_i + k][start_j + l] = 1
            
            # Recur
            backtrack(grid, min_squares)
            
            # Remove square and update min_squares
            for k in range(size):
                for l in range(size):
                    grid[start_i + k][start_j + l] = 0
            min_squares[0] = min(min_squares[0], 1 + min_squares[0])
        
        return min_squares[0]
    
    grid = [[0] * m for _ in range(n)]
    min_squares = [float('inf')]
    result = backtrack(grid, min_squares)
    return result

Solution = create_solution(tiling_rectangle)