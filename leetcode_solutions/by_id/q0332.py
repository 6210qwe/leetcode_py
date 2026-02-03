# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 332
标题: Reconstruct Itinerary
难度: hard
链接: https://leetcode.cn/problems/reconstruct-itinerary/
题目类型: 深度优先搜索、图、欧拉回路
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
332. 重新安排行程 - 给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi] 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。 所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。 * 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。 假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。 示例 1： [https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg] 输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] 输出：["JFK","MUC","LHR","SFO","SJC"] 示例 2： [https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg] 输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] 输出：["JFK","ATL","JFK","SFO","ATL","SFO"] 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。 提示： * 1 <= tickets.length <= 300 * tickets[i].length == 2 * fromi.length == 3 * toi.length == 3 * fromi 和 toi 由大写英文字母组成 * fromi != toi
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 欧拉回路，DFS+回溯，优先选择字典序小的

算法步骤:
1. 构建邻接表，按字典序排序
2. DFS遍历，优先选择字典序小的
3. 使用后序遍历，最后反转结果

关键点:
- 欧拉回路
- DFS+回溯
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(E log E) - E为边数
空间复杂度: O(E) - 邻接表和递归栈空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import defaultdict
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_itinerary(tickets: List[List[str]]) -> List[str]:
    """
    函数式接口 - 重新安排行程
    
    实现思路:
    欧拉回路：DFS+回溯，优先选择字典序小的。
    
    Args:
        tickets: 机票列表
        
    Returns:
        行程列表
        
    Example:
        >>> find_itinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
        ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']
    """
    graph = defaultdict(list)
    for src, dst in tickets:
        graph[src].append(dst)
    
    # 按字典序排序
    for src in graph:
        graph[src].sort()
    
    result = []
    
    def dfs(airport: str):
        """DFS遍历"""
        while graph[airport]:
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        result.append(airport)
    
    dfs("JFK")
    return result[::-1]


# 自动生成Solution类（无需手动编写）
Solution = create_solution(find_itinerary)
