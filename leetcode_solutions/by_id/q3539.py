# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3539
标题: Customer Purchasing Behavior Analysis
难度: medium
链接: https://leetcode.cn/problems/customer-purchasing-behavior-analysis/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3230. 客户购买行为分析 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来分析客户的购买行为

算法步骤:
1. 使用 GROUP BY 和 COUNT 来统计每个客户的购买次数
2. 使用 HAVING 子句来筛选出购买次数大于等于指定阈值的客户
3. 返回符合条件的客户列表

关键点:
- 使用 SQL 查询来高效地处理和分析数据
- 确保查询语句的正确性和效率
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是购买记录的数量。因为我们需要遍历所有的购买记录来进行分组和计数。
空间复杂度: O(1)，SQL 查询的空间复杂度主要取决于数据库的实现，但通常可以认为是常数级别的。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(purchases: List[dict], threshold: int) -> List[str]:
    """
    函数式接口 - 实现客户购买行为分析
    :param purchases: 购买记录列表，每个记录包含客户 ID 和购买信息
    :param threshold: 购买次数阈值
    :return: 购买次数大于等于阈值的客户列表
    """
    # 使用字典来统计每个客户的购买次数
    customer_counts = {}
    for purchase in purchases:
        customer_id = purchase['customer_id']
        if customer_id in customer_counts:
            customer_counts[customer_id] += 1
        else:
            customer_counts[customer_id] = 1

    # 筛选出购买次数大于等于阈值的客户
    result = [customer_id for customer_id, count in customer_counts.items() if count >= threshold]
    return result


Solution = create_solution(solution_function_name)