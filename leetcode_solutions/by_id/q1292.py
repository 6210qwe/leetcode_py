# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1292
标题: Immediate Food Delivery II
难度: medium
链接: https://leetcode.cn/problems/immediate-food-delivery-ii/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1174. 即时食物配送 II - 配送表: Delivery +-----------------------------+---------+ | Column Name | Type | +-----------------------------+---------+ | delivery_id | int | | customer_id | int | | order_date | date | | customer_pref_delivery_date | date | +-----------------------------+---------+ delivery_id 是该表中具有唯一值的列。 该表保存着顾客的食物配送信息，顾客在某个日期下了订单，并指定了一个期望的配送日期（和下单日期相同或者在那之后）。 如果顾客期望的配送日期和下单日期相同，则该订单称为 「即时订单」，否则称为「计划订单」。 「首次订单」是顾客最早创建的订单。我们保证一个顾客只会有一个「首次订单」。 编写解决方案以获取即时订单在所有用户的首次订单中的比例。保留两位小数。 结果示例如下所示： 示例 1： 输入： Delivery 表： +-------------+-------------+------------+-----------------------------+ | delivery_id | customer_id | order_date | customer_pref_delivery_date | +-------------+-------------+------------+-----------------------------+ | 1 | 1 | 2019-08-01 | 2019-08-02 | | 2 | 2 | 2019-08-02 | 2019-08-02 | | 3 | 1 | 2019-08-11 | 2019-08-12 | | 4 | 3 | 2019-08-24 | 2019-08-24 | | 5 | 3 | 2019-08-21 | 2019-08-22 | | 6 | 2 | 2019-08-11 | 2019-08-13 | | 7 | 4 | 2019-08-09 | 2019-08-09 | +-------------+-------------+------------+-----------------------------+ 输出： +----------------------+ | immediate_percentage | +----------------------+ | 50.00 | +----------------------+ 解释： 1 号顾客的 1 号订单是首次订单，并且是计划订单。 2 号顾客的 2 号订单是首次订单，并且是即时订单。 3 号顾客的 5 号订单是首次订单，并且是计划订单。 4 号顾客的 7 号订单是首次订单，并且是即时订单。 因此，一半顾客的首次订单是即时的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 
1. 找出每个顾客的首次订单。
2. 计算这些首次订单中即时订单的比例。

算法步骤:
1. 使用子查询找到每个顾客的首次订单。
2. 过滤出即时订单。
3. 计算即时订单的比例并保留两位小数。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 来找出每个顾客的首次订单。
- 使用条件聚合来计算即时订单的比例。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n) - 主要由排序操作决定。
空间复杂度: O(n) - 存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(delivery: List[List[str]]) -> float:
    """
    函数式接口 - 计算即时订单在所有用户的首次订单中的比例
    """
    import pandas as pd
    
    # 将输入数据转换为 DataFrame
    df = pd.DataFrame(delivery, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date'])
    
    # 转换日期格式
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['customer_pref_delivery_date'] = pd.to_datetime(df['customer_pref_delivery_date'])
    
    # 找出每个顾客的首次订单
    df['rank'] = df.groupby('customer_id')['order_date'].rank(method='dense')
    first_orders = df[df['rank'] == 1]
    
    # 计算即时订单的比例
    immediate_orders = first_orders[first_orders['order_date'] == first_orders['customer_pref_delivery_date']]
    immediate_percentage = (len(immediate_orders) / len(first_orders)) * 100
    
    return round(immediate_percentage, 2)


Solution = create_solution(solution_function_name)