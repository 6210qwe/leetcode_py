# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1215
标题: Reported Posts
难度: easy
链接: https://leetcode.cn/problems/reported-posts/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1113. 报告的记录 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个被举报的帖子的举报次数，并按要求格式化输出。

算法步骤:
1. 使用 `GROUP BY` 和 `COUNT` 函数来统计每个被举报帖子的举报次数。
2. 按照题目要求格式化输出结果。

关键点:
- 使用 `GROUP BY` 和 `COUNT` 函数来统计每个被举报帖子的举报次数。
- 确保输出格式符合题目要求。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 `actions` 表中的行数。我们需要遍历所有行来统计举报次数。
空间复杂度: O(1)，我们只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(actions: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 统计每个被举报帖子的举报次数，并按要求格式化输出。
    """
    from collections import defaultdict

    # 统计每个被举报帖子的举报次数
    report_count = defaultdict(int)
    for action in actions:
        if action[1] == "report":
            report_count[action[2]] += 1

    # 按要求格式化输出结果
    result = []
    for post_id, count in sorted(report_count.items(), key=lambda x: (-x[1], x[0])):
        result.append([post_id, str(count)])

    return result


Solution = create_solution(solution_function_name)