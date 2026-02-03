# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 302
标题: Smallest Rectangle Enclosing Black Pixels
难度: hard
链接: https://leetcode.cn/problems/smallest-rectangle-enclosing-black-pixels/
题目类型: 深度优先搜索、广度优先搜索、数组、二分查找、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
302. 包含全部黑色像素的最小矩形 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS或DFS找到所有黑色像素，计算边界

算法步骤:
1. 从给定点开始BFS/DFS找到所有黑色像素
2. 记录最小和最大的行、列坐标
3. 计算矩形面积

关键点:
- BFS/DFS遍历
- 时间复杂度O(m*n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n) - m*n为矩阵大小
空间复杂度: O(m*n) - 队列空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import deque
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_area(image: List[List[str]], x: int, y: int) -> int:
    """
    函数式接口 - 包含全部黑色像素的最小矩形
    
    实现思路:
    BFS找到所有黑色像素，计算边界。
    
    Args:
        image: 图像矩阵（'0'为白色，'1'为黑色）
        x: 起始行坐标
        y: 起始列坐标
        
    Returns:
        最小矩形面积
        
    Example:
        >>> min_area([["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], 0, 2)
        6
    """
    if not image or not image[0]:
        return 0
    
    m, n = len(image), len(image[0])
    min_row, max_row = x, x
    min_col, max_col = y, y
    
    queue = deque([(x, y)])
    visited = {(x, y)}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        i, j = queue.popleft()
        min_row = min(min_row, i)
        max_row = max(max_row, i)
        min_col = min(min_col, j)
        max_col = max(max_col, j)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and \
               image[ni][nj] == '1' and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append((ni, nj))
    
    return (max_row - min_row + 1) * (max_col - min_col + 1)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(min_area)
