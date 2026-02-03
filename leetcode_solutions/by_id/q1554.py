# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1554
标题: Minimum Time to Collect All Apples in a Tree
难度: medium
链接: https://leetcode.cn/problems/minimum-time-to-collect-all-apples-in-a-tree/
题目类型: 树、深度优先搜索、广度优先搜索、哈希表
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1443. 收集树上所有苹果的最少时间 - 给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从 节点 0 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。 无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 from 和 toi 。除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_1.png] 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false] 输出：8 解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。 示例 2： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_2.png] 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false] 输出：6 解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。 示例 3： 输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false] 输出：0 提示： * 1 <= n <= 10^5 * edges.length == n - 1 * edges[i].length == 2 * 0 <= ai < bi <= n - 1 * hasApple.length == n
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
