# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3865
标题: Find Product Recommendation Pairs
难度: medium
链接: https://leetcode.cn/problems/find-product-recommendation-pairs/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3521. 查找推荐产品对 - 表：ProductPurchases +-------------+------+ | Column Name | Type | +-------------+------+ | user_id | int | | product_id | int | | quantity | int | +-------------+------+ (user_id, product_id) 是这张表的唯一主键。 每一行代表用户以特定数量购买的产品。 表：ProductInfo +-------------+---------+ | Column Name | Type | +-------------+---------+ | product_id | int | | category | varchar | | price | decimal | +-------------+---------+ product_id 是这张表的唯一主键。 每一行表示一个产品的类别和价格。 亚马逊希望根据 共同购买模式 实现 “购买此商品的用户还购买了...” 功能。编写一个解决方案以实现： 1. 识别 被同一客户一起频繁购买的 不同 产品对（其中 product1_id < product2_id） 2. 对于 每个产品对，确定有多少客户购买了这两种产品 如果 至少有 3 位不同的 客户同时购买了这两种产品，则认为该 产品对 适合推荐。 返回结果表以 customer_count 降序 排序，并且为了避免排序持平，以 product1_id 升序 排序，并以 product2_id 升序 排序。 结果格式如下所示。 示例： 输入： ProductPurchases 表： +---------+------------+----------+ | user_id | product_id | quantity | +---------+------------+----------+ | 1 | 101 | 2 | | 1 | 102 | 1 | | 1 | 103 | 3 | | 2 | 101 | 1 | | 2 | 102 | 5 | | 2 | 104 | 1 | | 3 | 101 | 2 | | 3 | 103 | 1 | | 3 | 105 | 4 | | 4 | 101 | 1 | | 4 | 102 | 1 | | 4 | 103 | 2 | | 4 | 104 | 3 | | 5 | 102 | 2 | | 5 | 104 | 1 | +---------+------------+----------+ ProductInfo 表： +------------+-------------+-------+ | product_id | category | price | +------------+-------------+-------+ | 101 | Electronics | 100 | | 102 | Books | 20 | | 103 | Clothing | 35 | | 104 | Kitchen | 50 | | 105 | Sports | 75 | +------------+-------------+-------+ 输出： +-------------+-------------+-------------------+-------------------+----------------+ | product1_id | product2_id | product1_category | product2_category | customer_count | +-------------+-------------+-------------------+-------------------+----------------+ | 101 | 102 | Electronics | Books | 3 | | 101 | 103 | Electronics | Clothing | 3 | | 102 | 104 | Books | Kitchen | 3 | +-------------+-------------+-------------------+-------------------+----------------+ 解释： * 产品对 (101, 102)： * 被用户 1，2 和 4 购买（3 个消费者） * 产品 101 属于电子商品类别 * 产品 102 属于图书类别 * 产品对 (101, 103)： * 被用户 1，3 和 4 购买（3 个消费者） * 产品 101 属于电子商品类别 * 产品 103 属于服装类别 * 产品对 (102, 104)： * 被用户 2，4 和 5 购买（3 个消费者） * 产品 102 属于图书类别 * 产品 104 属于厨房用品类别 结果以 customer_count 降序排序。对于有相同 customer_count 的产品对，将它们以 product1_id 升序排序，然后以 product2_id 升序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用自连接和聚合函数来找出共同购买的产品对，并计算每个产品对的购买用户数。

算法步骤:
1. 使用自连接找到所有可能的产品对 (product1_id, product2_id)，确保 product1_id < product2_id。
2. 计算每对产品被多少个不同的用户购买。
3. 过滤出至少有 3 个不同用户购买的产品对。
4. 将结果与 ProductInfo 表连接，获取每个产品的类别。
5. 按照 customer_count 降序、product1_id 升序、product2_id 升序排序。

关键点:
- 使用自连接和聚合函数来处理数据。
- 确保 product1_id < product2_id 以避免重复的产品对。
- 使用 GROUP BY 和 HAVING 来过滤出符合条件的产品对。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 ProductPurchases 表中的行数。自连接操作的时间复杂度是 O(n^2)。
空间复杂度: O(n^2)，用于存储自连接后的结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd

def solution_function_name(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    # 自连接找到所有可能的产品对 (product1_id, product2_id)，确保 product1_id < product2_id
    pairs = product_purchases.merge(
        product_purchases, on='user_id', suffixes=('_1', '_2')
    ).query('product_id_1 < product_id_2')

    # 计算每对产品被多少个不同的用户购买
    pair_counts = pairs.groupby(['product_id_1', 'product_id_2'])['user_id'].nunique().reset_index()
    pair_counts.columns = ['product1_id', 'product2_id', 'customer_count']

    # 过滤出至少有 3 个不同用户购买的产品对
    recommended_pairs = pair_counts.query('customer_count >= 3')

    # 将结果与 ProductInfo 表连接，获取每个产品的类别
    result = recommended_pairs.merge(
        product_info, left_on='product1_id', right_on='product_id'
    ).merge(
        product_info, left_on='product2_id', right_on='product_id', suffixes=('_1', '_2')
    )

    # 选择需要的列并重命名
    result = result[['product1_id', 'product2_id', 'category_1', 'category_2', 'customer_count']]
    result.columns = ['product1_id', 'product2_id', 'product1_category', 'product2_category', 'customer_count']

    # 按照 customer_count 降序、product1_id 升序、product2_id 升序排序
    result = result.sort_values(by=['customer_count', 'product1_id', 'product2_id'], ascending=[False, True, True])

    return result

Solution = create_solution(solution_function_name)