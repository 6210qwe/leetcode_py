# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1578
标题: Apples & Oranges
难度: medium
链接: https://leetcode.cn/problems/apples-oranges/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1445. 苹果和桔子 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计苹果和桔子的数量。

算法步骤:
1. 构建 SQL 查询语句，从表中选择苹果和桔子的数量。
2. 执行查询并返回结果。

关键点:
- 使用 SQL 的 COUNT 函数来统计数量。
- 确保查询条件正确区分苹果和桔子。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是表中的行数。SQL 查询需要遍历整个表来统计数量。
空间复杂度: O(1)，查询结果只包含两个整数，不随输入规模增加而增加。
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
    函数式接口 - 实现 SQL 查询来统计苹果和桔子的数量
    """
    # SQL 查询语句
    query = """
    SELECT 
        SUM(CASE WHEN fruit = 'apple' THEN 1 ELSE 0 END) AS apple_count,
        SUM(CASE WHEN fruit = 'orange' THEN 1 ELSE 0 END) AS orange_count
    FROM fruits
    """
    
    # 假设 params 是一个数据库连接对象
    cursor = params.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    
    return result['apple_count'], result['orange_count']


Solution = create_solution(solution_function_name)