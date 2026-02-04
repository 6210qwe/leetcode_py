# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1318
标题: Tournament Winners
难度: hard
链接: https://leetcode.cn/problems/tournament-winners/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1194. 锦标赛优胜者 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个队伍的得分，并根据得分排序选出前几名。

算法步骤:
1. 创建一个临时表来记录每场比赛的结果。
2. 计算每个队伍的得分。
3. 根据得分对队伍进行排序。
4. 选择前几名队伍作为优胜者。

关键点:
- 使用子查询和窗口函数来计算每个队伍的得分。
- 使用 `RANK()` 函数来对队伍进行排名。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是比赛的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，需要存储比赛结果和队伍得分。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(matches: List[List[int]]) -> List[List[int]]:
    """
    函数式接口 - 实现锦标赛优胜者的计算
    """
    from collections import defaultdict
    import pandas as pd

    # 1. 创建一个临时表来记录每场比赛的结果
    match_results = []
    for match in matches:
        winner, loser, points = match
        match_results.append((winner, points))
        match_results.append((loser, 0))

    # 2. 计算每个队伍的得分
    score_table = defaultdict(int)
    for team, points in match_results:
        score_table[team] += points

    # 3. 将得分转换为 DataFrame 并进行排序
    df = pd.DataFrame(list(score_table.items()), columns=['team', 'score'])
    df['rank'] = df['score'].rank(method='dense', ascending=False)

    # 4. 选择前几名队伍作为优胜者
    top_teams = df[df['rank'] == 1][['team', 'score']].values.tolist()

    return top_teams

Solution = create_solution(solution_function_name)