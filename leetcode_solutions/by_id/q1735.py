# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1735
标题: The Most Frequently Ordered Products for Each Customer
难度: medium
链接: https://leetcode.cn/problems/the-most-frequently-ordered-products-for-each-customer/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1596. 每位顾客最经常订购的商品 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Pandas 库来处理数据，通过分组和聚合操作找到每位顾客最经常订购的商品。

算法步骤:
1. 读取订单数据并进行预处理。
2. 使用 `groupby` 和 `agg` 方法按顾客和产品分组，并计算每个产品的订购次数。
3. 找出每位顾客订购次数最多的产品。
4. 返回结果。

关键点:
- 使用 Pandas 的 `groupby` 和 `agg` 方法进行高效的分组和聚合操作。
- 使用 `transform` 方法找到每个分组的最大值。
- 使用 `query` 方法筛选出订购次数最多的产品。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是订单的数量。主要的时间开销在于排序和分组操作。
空间复杂度: O(n)，需要存储分组后的数据。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd


def find_frequent_products(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 找到每位顾客最经常订购的商品
    """
    # 合并 customers 和 orders 表
    merged_df = pd.merge(customers, orders, on='customer_id')
    
    # 按 customer_id 和 product_name 分组，并计算每个产品的订购次数
    grouped_df = merged_df.groupby(['customer_id', 'product_name']).size().reset_index(name='order_count')
    
    # 找到每个 customer_id 的最大 order_count
    max_counts = grouped_df.groupby('customer_id')['order_count'].transform('max')
    
    # 筛选出订购次数最多的产品
    result_df = grouped_df[grouped_df['order_count'] == max_counts]
    
    # 选择需要的列并重命名
    result_df = result_df[['customer_id', 'customer_name', 'product_name']].rename(columns={'customer_name': 'customer_name'})
    
    return result_df


Solution = create_solution(find_frequent_products)