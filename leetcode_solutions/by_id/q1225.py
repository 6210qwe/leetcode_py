# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1225
标题: Active Businesses
难度: medium
链接: https://leetcode.cn/problems/active-businesses/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1126. 查询活跃业务 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来找出活跃的业务。

算法步骤:
1. 创建一个临时表 `temp` 来存储每个业务在每个事件类型中的活动次数。
2. 从 `temp` 表中筛选出满足条件的业务，即在每个事件类型中的活动次数都大于等于该事件类型的阈值。

关键点:
- 使用 GROUP BY 和 HAVING 子句来筛选出符合条件的业务。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * m)，其中 n 是 events 表的行数，m 是不同 event_type 的数量。
空间复杂度: O(n * m)，用于存储临时表 `temp`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(events: List[List[str]], threshold: int) -> List[str]:
    """
    函数式接口 - 实现查询活跃业务
    """
    # 创建一个字典来存储每个业务在每个事件类型中的活动次数
    business_activity = {}
    
    # 遍历 events 表，统计每个业务在每个事件类型中的活动次数
    for business, event_type in events:
        if business not in business_activity:
            business_activity[business] = {}
        if event_type not in business_activity[business]:
            business_activity[business][event_type] = 0
        business_activity[business][event_type] += 1
    
    # 筛选出满足条件的业务
    active_businesses = []
    for business, activity in business_activity.items():
        if all(count >= threshold for count in activity.values()):
            active_businesses.append(business)
    
    return active_businesses


Solution = create_solution(solution_function_name)