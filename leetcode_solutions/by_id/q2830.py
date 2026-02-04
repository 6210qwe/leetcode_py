# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2830
标题: Count Artist Occurrences On Spotify Ranking List
难度: easy
链接: https://leetcode.cn/problems/count-artist-occurrences-on-spotify-ranking-list/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2669. 统计 Spotify 排行榜上艺术家出现次数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个艺术家在排行榜上的出现次数。

算法步骤:
1. 使用 GROUP BY 子句按艺术家分组。
2. 使用 COUNT 函数统计每个艺术家的出现次数。

关键点:
- 使用 SQL 的 GROUP BY 和 COUNT 函数来实现高效的统计。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是排行榜上的歌曲数量。需要遍历整个排行榜来统计每个艺术家的出现次数。
空间复杂度: O(m)，其中 m 是不同艺术家的数量。需要存储每个艺术家的出现次数。
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
    函数式接口 - 实现
    """
    # 实现最优解法
    query = """
    SELECT artist, COUNT(*) AS occurrences
    FROM ranking_list
    GROUP BY artist;
    """
    return query


Solution = create_solution(solution_function_name)