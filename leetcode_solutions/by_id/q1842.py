# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1842
标题: Number of Calls Between Two Persons
难度: medium
链接: https://leetcode.cn/problems/number-of-calls-between-two-persons/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1699. 两人之间的通话次数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计两人之间的通话次数。

算法步骤:
1. 创建一个临时表 `calls` 来存储所有通话记录。
2. 使用 `UNION ALL` 将每个通话记录的两个方向都插入到临时表中。
3. 使用 `GROUP BY` 和 `COUNT` 来统计每对通话者之间的通话次数。

关键点:
- 使用 `UNION ALL` 来处理双向通话记录。
- 使用 `GROUP BY` 和 `COUNT` 来统计通话次数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是通话记录的数量。我们需要遍历所有通话记录并进行分组统计。
空间复杂度: O(n)，临时表 `calls` 的大小与输入数据量成正比。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(calls: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 统计两人之间的通话次数
    """
    # 创建一个字典来存储每对通话者的通话次数
    call_count = {}
    
    # 遍历所有通话记录，并更新通话次数
    for caller, callee in calls:
        key1 = (caller, callee)
        key2 = (callee, caller)
        
        if key1 in call_count:
            call_count[key1] += 1
        else:
            call_count[key1] = 1
        
        if key2 in call_count:
            call_count[key2] += 1
        else:
            call_count[key2] = 1
    
    # 构建结果列表
    result = []
    for (caller, callee), count in call_count.items():
        result.append([caller, callee, str(count)])
    
    return result


Solution = create_solution(solution_function_name)