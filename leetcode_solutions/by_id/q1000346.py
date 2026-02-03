# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000346
标题: 省份数量
难度: medium
链接: https://leetcode.cn/problems/bLyHh0/
题目类型: 深度优先搜索、广度优先搜索、并查集、图
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 116. 省份数量 - 有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。 省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。 给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。 返回矩阵中 省份 的数量。 示例 1： [https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg] 输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]] 输出：2 示例 2： [https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg] 输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]] 输出：3 提示： * 1 <= n <= 200 * n == isConnected.length * n == isConnected[i].length * isConnected[i][j] 为 1 或 0 * isConnected[i][i] == 1 * isConnected[i][j] == isConnected[j][i] 注意：本题与主站 547 题相同： https://leetcode.cn/problems/number-of-provinces/ [https://leetcode.cn/problems/number-of-provinces/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: DFS或并查集，找连通分量数量

算法步骤:
1. 使用DFS遍历所有城市
2. 对每个未访问的城市，进行DFS标记所有连通城市
3. 连通分量的数量就是省份数量

关键点:
- DFS或并查集
- 时间复杂度O(n^2)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2) - 遍历邻接矩阵
空间复杂度: O(n) - 访问数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_circle_num(isConnected: List[List[int]]) -> int:
    """
    函数式接口 - 省份数量
    
    实现思路:
    DFS：遍历所有城市，统计连通分量数量。
    
    Args:
        isConnected: 邻接矩阵
        
    Returns:
        省份数量
        
    Example:
        >>> find_circle_num([[1,1,0],[1,1,0],[0,0,1]])
        2
    """
    n = len(isConnected)
    visited = [False] * n
    count = 0
    
    def dfs(city: int):
        """DFS遍历连通的城市"""
        visited[city] = True
        for i in range(n):
            if isConnected[city][i] == 1 and not visited[i]:
                dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    
    return count


Solution = create_solution(find_circle_num)
