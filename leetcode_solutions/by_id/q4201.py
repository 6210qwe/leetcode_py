# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 4201
标题: Design Order Management System
难度: medium
链接: https://leetcode.cn/problems/design-order-management-system/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3822. 设计订单管理系统 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典来存储订单，并使用两个堆来维护最新的订单和历史订单。

算法步骤:
1. 初始化订单管理系统，创建两个堆（最大堆和最小堆）以及一个字典来存储订单。
2. 实现添加订单的方法，将订单添加到字典中，并更新堆。
3. 实现获取最新订单的方法，从最大堆中获取。
4. 实现获取历史订单的方法，从最小堆中获取。

关键点:
- 使用堆来高效地获取最新的订单和历史订单。
- 使用字典来快速查找和更新订单。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 添加订单和获取订单的时间复杂度主要由堆操作决定。
空间复杂度: O(n) - 存储订单所需的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import heapq

class OrderManagementSystem:
    def __init__(self):
        self.orders = {}  # 存储订单的字典
        self.latest_orders = []  # 最大堆，用于获取最新订单
        self.history_orders = []  # 最小堆，用于获取历史订单
        self.order_id = 0  # 订单ID生成器

    def add_order(self, order: str) -> int:
        """
        添加订单并返回订单ID
        """
        self.order_id += 1
        order_id = self.order_id
        self.orders[order_id] = order
        heapq.heappush(self.latest_orders, (-order_id, order))
        heapq.heappush(self.history_orders, (order_id, order))
        return order_id

    def get_latest_order(self) -> Optional[str]:
        """
        获取最新的订单
        """
        while self.latest_orders and -self.latest_orders[0][0] not in self.orders:
            heapq.heappop(self.latest_orders)
        if self.latest_orders:
            _, order = self.latest_orders[0]
            return order
        return None

    def get_history_order(self) -> Optional[str]:
        """
        获取历史订单
        """
        while self.history_orders and self.history_orders[0][0] not in self.orders:
            heapq.heappop(self.history_orders)
        if self.history_orders:
            _, order = self.history_orders[0]
            return order
        return None

# 工厂函数
def create_solution():
    return OrderManagementSystem()

# 示例调用
# solution = create_solution()
# order_id = solution.add_order("Order 1")
# print(solution.get_latest_order())
# print(solution.get_history_order())

Solution = create_solution()