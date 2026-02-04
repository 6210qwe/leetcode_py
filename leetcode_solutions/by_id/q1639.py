# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1639
标题: Friendly Movies Streamed Last Month
难度: easy
链接: https://leetcode.cn/problems/friendly-movies-streamed-last-month/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1495. 上月播放的儿童适宜电影 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来筛选出上个月播放的儿童适宜电影。

算法步骤:
1. 选择 `title` 列。
2. 从 `Movies` 表中筛选出 `description` 不包含 'not' 的记录。
3. 进一步筛选出 `date_added` 在上个月的记录。
4. 按 `title` 升序排序。

关键点:
- 使用 `LIKE` 和 `NOT LIKE` 来过滤描述。
- 使用 `DATE_FORMAT` 和 `BETWEEN` 来筛选日期范围。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是表中的行数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，SQL 查询的空间复杂度通常为常数级别。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name():
    """
    函数式接口 - 实现最优解法
    """
    query = """
    SELECT title
    FROM Movies
    WHERE description NOT LIKE '%not%'
      AND date_added BETWEEN DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 1 MONTH), '%Y-%m-01') 
                        AND LAST_DAY(DATE_SUB(CURDATE(), INTERVAL 1 MONTH))
    ORDER BY title ASC;
    """
    return query


Solution = create_solution(solution_function_name)