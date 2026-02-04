# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3650
标题: Find Cities in Each State II
难度: medium
链接: https://leetcode.cn/problems/find-cities-in-each-state-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3328. 查找每个州的城市 II - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来获取每个州的城市列表，并按要求排序。

算法步骤:
1. 从 `Cities` 表中选择所有城市及其对应的州。
2. 按照州名和城市名进行排序。
3. 使用 GROUP BY 和 GROUP_CONCAT 函数将每个州的城市名拼接成一个字符串。
4. 返回结果集。

关键点:
- 使用 GROUP_CONCAT 函数将城市名拼接成一个字符串。
- 确保结果按州名和城市名排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `Cities` 表中的行数。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，查询过程中使用的额外空间是常数级别的。
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

# SQL 查询实现
def find_cities_in_each_state() -> str:
    query = """
    SELECT 
        state, 
        GROUP_CONCAT(city ORDER BY city ASC SEPARATOR ', ') AS cities
    FROM 
        Cities
    GROUP BY 
        state
    ORDER BY 
        state ASC;
    """
    return query

# 示例调用
print(find_cities_in_each_state())