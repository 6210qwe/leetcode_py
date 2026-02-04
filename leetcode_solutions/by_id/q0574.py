# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 574
标题: Winning Candidate
难度: medium
链接: https://leetcode.cn/problems/winning-candidate/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
574. 当选者 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找到获胜的候选人。

算法步骤:
1. 创建一个临时表来计算每个候选人的总票数。
2. 从临时表中选择票数最多的候选人。
3. 如果有多个候选人票数相同且最高，则选择名字字典序最小的候选人。

关键点:
- 使用子查询和聚合函数来计算每个候选人的票数。
- 使用 `ORDER BY` 和 `LIMIT` 来获取票数最多且名字字典序最小的候选人。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是投票记录的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，需要存储每个候选人的票数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(votes: List[List[str]]) -> str:
    """
    函数式接口 - 找到获胜的候选人
    """
    from collections import defaultdict
    import heapq

    # 计算每个候选人的票数
    vote_count = defaultdict(int)
    for _, candidate in votes:
        vote_count[candidate] += 1

    # 使用最大堆来找到票数最多且名字字典序最小的候选人
    max_heap = [(-count, candidate) for candidate, count in vote_count.items()]
    heapq.heapify(max_heap)

    # 获取票数最多且名字字典序最小的候选人
    _, winner = heapq.heappop(max_heap)
    return winner


Solution = create_solution(solution_function_name)