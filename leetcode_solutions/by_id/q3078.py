# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3078
标题: Election Results
难度: medium
链接: https://leetcode.cn/problems/election-results/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2820. 选举结果 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来记录每个候选人的得票数，并找到得票最多的候选人。

算法步骤:
1. 初始化一个哈希表 `votes` 来记录每个候选人的得票数。
2. 遍历选票数组 `persons` 和 `votes_num`，更新哈希表中的得票数。
3. 找到得票最多的候选人，并返回其名字。

关键点:
- 使用哈希表来高效地记录和查找每个候选人的得票数。
- 通过遍历一次选票数组来完成计票。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是选票数组的长度。我们只需要遍历一次选票数组。
空间复杂度: O(m)，其中 m 是候选人的数量。我们需要一个哈希表来记录每个候选人的得票数。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(persons: List[int], votes_num: List[int]) -> str:
    """
    函数式接口 - 返回得票最多的候选人名字
    """
    # 初始化哈希表来记录每个候选人的得票数
    votes = {}
    
    # 遍历选票数组，更新哈希表中的得票数
    for person, vote in zip(persons, votes_num):
        if person not in votes:
            votes[person] = 0
        votes[person] += vote
    
    # 找到得票最多的候选人
    max_votes = 0
    winner = None
    for person, vote in votes.items():
        if vote > max_votes:
            max_votes = vote
            winner = person
    
    return winner


Solution = create_solution(solution_function_name)