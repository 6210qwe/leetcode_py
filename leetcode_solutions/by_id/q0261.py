# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 261
标题: Graph Valid Tree
难度: medium
链接: https://leetcode.cn/problems/graph-valid-tree/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
261. 以图判树 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 并查集或DFS，判断是否为树

算法步骤:
1. 树的条件：n个节点，n-1条边，且连通
2. 使用并查集检查是否有环
3. 检查是否所有节点连通

关键点:
- 并查集检测环
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


def valid_tree(n: int, edges: List[List[int]]) -> bool:
    """
    函数式接口 - 以图判树
    
    实现思路:
    并查集：检查是否有环且连通。
    
    Args:
        n: 节点数
        edges: 边数组
        
    Returns:
        是否为有效的树
        
    Example:
        >>> valid_tree(5, [[0,1],[0,2],[0,3],[1,4]])
        True
    """
    # 树的条件：n个节点，n-1条边
    if len(edges) != n - 1:
        return False
    
    # 并查集
    parent = list(range(n))
    
    def find(x: int) -> int:
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x: int, y: int) -> bool:
        px, py = find(x), find(y)
        if px == py:
            return False  # 有环
        parent[px] = py
        return True
    
    # 检查每条边
    for x, y in edges:
        if not union(x, y):
            return False
    
    # 检查是否所有节点连通
    root = find(0)
    return all(find(i) == root for i in range(n))


# 自动生成Solution类（无需手动编写）
Solution = create_solution(valid_tree)
