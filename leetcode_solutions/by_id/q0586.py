# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 586
标题: Customer Placing the Largest Number of Orders
难度: easy
链接: https://leetcode.cn/problems/customer-placing-the-largest-number-of-orders/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
586. 订单最多的客户 - 表: Orders +-----------------+----------+ | Column Name | Type | +-----------------+----------+ | order_number | int | | customer_number | int | +-----------------+----------+ 在 SQL 中，Order_number是该表的主键。 此表包含关于订单ID和客户ID的信息。 查找下了 最多订单 的客户的 customer_number 。 测试用例生成后， 恰好有一个客户 比任何其他客户下了更多的订单。 查询结果格式如下所示。 示例 1: 输入: Orders 表: +--------------+-----------------+ | order_number | customer_number | +--------------+-----------------+ | 1 | 1 | | 2 | 2 | | 3 | 3 | | 4 | 3 | +--------------+-----------------+ 输出: +-----------------+ | customer_number | +-----------------+ | 3 | +-----------------+ 解释: customer_number 为 '3' 的顾客有两个订单，比顾客 '1' 或者 '2' 都要多，因为他们只有一个订单。 所以结果是该顾客的 customer_number ，也就是 3 。 进阶： 如果有多位顾客订单数并列最多，你能找到他们所有的 customer_number 吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典统计每个客户的订单数量，然后找到订单数量最多的客户。

算法步骤:
1. 创建一个字典来统计每个客户的订单数量。
2. 遍历订单表，更新字典中的订单数量。
3. 找到订单数量最多的客户。

关键点:
- 使用字典进行高效的计数。
- 一次遍历即可完成统计。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是订单表的长度。我们需要遍历整个订单表一次。
空间复杂度: O(m)，其中 m 是不同客户的数量。我们需要存储每个客户的订单数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(orders: List[List[int]]) -> int:
    """
    函数式接口 - 实现查找订单最多的客户
    """
    # 统计每个客户的订单数量
    order_count = {}
    for _, customer_number in orders:
        if customer_number in order_count:
            order_count[customer_number] += 1
        else:
            order_count[customer_number] = 1
    
    # 找到订单数量最多的客户
    max_orders = max(order_count.values())
    for customer, count in order_count.items():
        if count == max_orders:
            return customer

Solution = create_solution(solution_function_name)