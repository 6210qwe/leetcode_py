# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 305
标题: Number of Islands II
难度: hard
链接: https://leetcode.cn/problems/number-of-islands-ii/
题目类型: 并查集、数组、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
305. 岛屿数量 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用并查集，每次添加一个陆地时，检查并合并相邻的陆地

算法步骤:
1. 初始化并查集
2. 对于每个操作，添加陆地并检查四个方向的相邻位置
3. 如果相邻位置是陆地，合并两个连通分量
4. 记录每次操作后的岛屿数量

关键点:
- 使用并查集维护连通分量
- 时间复杂度O(k*α(mn))，k为操作数，α为反阿克曼函数
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(k*α(mn)) - k为操作数，α为反阿克曼函数
空间复杂度: O(mn) - 并查集空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


class UnionFind:
    """并查集"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = 0
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            self.count -= 1
            return True
        return False
    
    def add_land(self):
        self.count += 1


def number_of_islands_ii(m: int, n: int, positions: List[List[int]]) -> List[int]:
    """
    函数式接口 - 岛屿数量II
    
    实现思路:
    使用并查集，每次添加一个陆地时，检查并合并相邻的陆地。
    
    Args:
        m: 网格行数
        n: 网格列数
        positions: 操作列表，每个元素为[row, col]
        
    Returns:
        每次操作后的岛屿数量列表
        
    Example:
        >>> number_of_islands_ii(3, 3, [[0,0],[0,1],[1,2],[2,1]])
        [1, 1, 2, 3]
    """
    uf = UnionFind(m * n)
    grid = [[0] * n for _ in range(m)]
    result = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for row, col in positions:
        if grid[row][col] == 1:
            result.append(uf.count)
            continue
        
        grid[row][col] = 1
        uf.add_land()
        pos = row * n + col
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                neighbor_pos = nr * n + nc
                uf.union(pos, neighbor_pos)
        
        result.append(uf.count)
    
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(number_of_islands_ii)
