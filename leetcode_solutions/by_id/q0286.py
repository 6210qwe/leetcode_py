# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 286
标题: Walls and Gates
难度: medium
链接: https://leetcode.cn/problems/walls-and-gates/
题目类型: 广度优先搜索、数组、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
286. 墙与门 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: BFS从所有门开始，计算到每个空房间的最短距离

算法步骤:
1. 将所有门的位置加入队列
2. BFS遍历，更新空房间的距离
3. 跳过墙和已访问的房间

关键点:
- BFS多源点
- 时间复杂度O(m*n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(m*n) - 遍历所有格子
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


def walls_and_gates(rooms: List[List[int]]) -> None:
    """
    函数式接口 - 墙与门
    
    实现思路:
    BFS从所有门开始，计算到每个空房间的最短距离。
    
    Args:
        rooms: 房间矩阵（-1为墙，0为门，INF为空房间）
        
    Returns:
        None（原地修改）
        
    Example:
        >>> rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
        >>> walls_and_gates(rooms)
    """
    if not rooms or not rooms[0]:
        return
    
    m, n = len(rooms), len(rooms[0])
    INF = 2147483647
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    
    # 将所有门加入队列
    for i in range(m):
        for j in range(n):
            if rooms[i][j] == 0:
                queue.append((i, j))
    
    # BFS
    while queue:
        i, j = queue.popleft()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == INF:
                rooms[ni][nj] = rooms[i][j] + 1
                queue.append((ni, nj))


# 自动生成Solution类（无需手动编写）
Solution = create_solution(walls_and_gates)
