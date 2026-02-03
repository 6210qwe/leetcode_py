# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 323
标题: Number of Connected Components in an Undirected Graph
难度: medium
链接: https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
323. 无向图中连通分量的数目 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 并查集或DFS，统计连通分量数量

算法步骤:
1. 使用并查集合并所有边
2. 统计不同根节点的数量

关键点:
- 并查集
- 时间复杂度O(n)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - n为节点数
空间复杂度: O(n) - 并查集空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def count_components(n: int, edges: List[List[int]]) -> int:
    """
    函数式接口 - 无向图中连通分量的数目
    
    实现思路:
    并查集：合并所有边，统计不同根节点的数量。
    
    Args:
        n: 节点数
        edges: 边数组
        
    Returns:
        连通分量数量
        
    Example:
        >>> count_components(5, [[0,1],[1,2],[3,4]])
        2
    """
    parent = list(range(n))
    
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
    
    for x, y in edges:
        union(x, y)
    
    # 统计不同根节点的数量
    roots = set()
    for i in range(n):
        roots.add(find(i))
    
    return len(roots)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(count_components)
