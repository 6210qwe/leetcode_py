# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1237
标题: Reported Posts II
难度: medium
链接: https://leetcode.cn/problems/reported-posts-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1132. 报告的记录 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计每个用户的报告数量，并按要求进行排序和过滤。

算法步骤:
1. 使用子查询计算每个被举报用户的报告次数。
2. 过滤出报告次数大于等于指定阈值的用户。
3. 按照报告次数降序排列，如果报告次数相同，则按用户ID升序排列。

关键点:
- 使用 GROUP BY 和 COUNT 函数来统计报告次数。
- 使用 HAVING 子句来过滤报告次数大于等于指定阈值的用户。
- 使用 ORDER BY 子句来排序结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是报告记录的数量。主要的时间消耗在于排序操作。
空间复杂度: O(n)，用于存储中间结果和最终结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(reports: List[List[str]], threshold: int) -> List[List[str]]:
    """
    函数式接口 - 实现
    :param reports: 报告记录列表，每个元素为 [reporter_id, reported_id]
    :param threshold: 报告次数的阈值
    :return: 满足条件的用户列表
    """
    from collections import defaultdict
    report_count = defaultdict(int)
    
    # 统计每个被举报用户的报告次数
    for _, reported_id in reports:
        report_count[reported_id] += 1
    
    # 过滤出报告次数大于等于阈值的用户
    result = [[reported_id, count] for reported_id, count in report_count.items() if count >= threshold]
    
    # 按报告次数降序排列，如果报告次数相同，则按用户ID升序排列
    result.sort(key=lambda x: (-x[1], x[0]))
    
    return result


Solution = create_solution(solution_function_name)