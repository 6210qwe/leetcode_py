# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 863
标题: Sum of Distances in Tree
难度: hard
链接: https://leetcode.cn/problems/sum-of-distances-in-tree/
题目类型: 树、深度优先搜索、图、动态规划
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
834. 树中距离之和 - 给定一个无向、连通的树。树中有 n 个标记为 0...n-1 的节点以及 n-1 条边 。 给定整数 n 和数组 edges ， edges[i] = [ai, bi]表示树中的节点 ai 和 bi 之间有一条边。 返回长度为 n 的数组 answer ，其中 answer[i] 是树中第 i 个节点与所有其他节点之间的距离之和。 示例 1: [https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist1.jpg] 输入: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]] 输出: [8,12,6,10,10,10] 解释: 树如图所示。 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。 示例 2: [https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist2.jpg] 输入: n = 1, edges = [] 输出: [0] 示例 3: [https://assets.leetcode.com/uploads/2021/07/23/lc-sumdist3.jpg] 输入: n = 2, edges = [[1,0]] 输出: [1,1] 提示: * 1 <= n <= 3 * 104 * edges.length == n - 1 * edges[i].length == 2 * 0 <= ai, bi < n * ai != bi * 给定的输入保证为有效的树
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
