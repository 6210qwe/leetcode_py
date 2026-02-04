# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2501
标题: Generate the Invoice
难度: hard
链接: https://leetcode.cn/problems/generate-the-invoice/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2362. 生成发票 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来生成发票

算法步骤:
1. 计算每个订单的总价
2. 生成包含订单详情和总价的发票

关键点:
- 使用子查询计算每个订单的总价
- 使用 JOIN 操作将订单详情和总价合并
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是订单表的行数，m 是订单详情表的行数
空间复杂度: O(1)，假设数据库查询的中间结果不会占用额外的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def generate_invoice(orders: List[dict], order_items: List[dict]) -> List[dict]:
    """
    生成发票
    :param orders: 订单列表
    :param order_items: 订单详情列表
    :return: 发票列表
    """
    # 计算每个订单的总价
    order_totals = {}
    for item in order_items:
        order_id = item['order_id']
        if order_id not in order_totals:
            order_totals[order_id] = 0
        order_totals[order_id] += item['quantity'] * item['price']

    # 生成发票
    invoices = []
    for order in orders:
        order_id = order['id']
        total_price = order_totals.get(order_id, 0)
        invoice = {
            'order_id': order_id,
            'customer_name': order['customer_name'],
            'total_price': total_price
        }
        invoices.append(invoice)

    return invoices


Solution = create_solution(generate_invoice)