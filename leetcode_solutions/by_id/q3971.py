# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3971
标题: Find Stores with Inventory Imbalance
难度: medium
链接: https://leetcode.cn/problems/find-stores-with-inventory-imbalance/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3626. 查找库存不平衡的店铺 - 表：stores +-------------+---------+ | Column Name | Type | +-------------+---------+ | store_id | int | | store_name | varchar | | location | varchar | +-------------+---------+ store_id 是这张表的唯一主键。 每一行包含有关商店及其位置的信息。 表：inventory +-------------+---------+ | Column Name | Type | +-------------+---------+ | inventory_id| int | | store_id | int | | product_name| varchar | | quantity | int | | price | decimal | +-------------+---------+ inventory_id 是这张表的唯一主键。 每一行代表特定商店中某一特定产品的库存情况。 编写一个解决方案来查找库存不平衡的商店 - 即最贵商品的库存比最便宜商品少的商店。 * 对于每个商店，识别 最贵的商品（最高价格）及其数量，如果有多个最贵的商品则选取数量最多的一个。 * 对于每个商店，识别 最便宜的商品（最低价格）及其数量，如果有多个最便宜的物品则选取数量最多的一个。 * 如果最贵商品的数量 少于 最便宜商品的数量，则商店存在库存不平衡。 * 按（最便宜商品的数量/最贵商品的数量）计算 不平衡比。 * 不平衡比 舍入到 2 位 小数 * 结果只包含 至少有 3 个不同商品 的店铺 返回结果表以不平衡比率降序排列，然后按商店名称升序排列。 结果格式如下所示。 示例： 输入： stores 表： +----------+----------------+-------------+ | store_id | store_name | location | +----------+----------------+-------------+ | 1 | Downtown Tech | New York | | 2 | Suburb Mall | Chicago | | 3 | City Center | Los Angeles | | 4 | Corner Shop | Miami | | 5 | Plaza Store | Seattle | +----------+----------------+-------------+ inventory 表： +--------------+----------+--------------+----------+--------+ | inventory_id | store_id | product_name | quantity | price | +--------------+----------+--------------+----------+--------+ | 1 | 1 | Laptop | 5 | 999.99 | | 2 | 1 | Mouse | 50 | 19.99 | | 3 | 1 | Keyboard | 25 | 79.99 | | 4 | 1 | Monitor | 15 | 299.99 | | 5 | 2 | Phone | 3 | 699.99 | | 6 | 2 | Charger | 100 | 25.99 | | 7 | 2 | Case | 75 | 15.99 | | 8 | 2 | Headphones | 20 | 149.99 | | 9 | 3 | Tablet | 2 | 499.99 | | 10 | 3 | Stylus | 80 | 29.99 | | 11 | 3 | Cover | 60 | 39.99 | | 12 | 4 | Watch | 10 | 299.99 | | 13 | 4 | Band | 25 | 49.99 | | 14 | 5 | Camera | 8 | 599.99 | | 15 | 5 | Lens | 12 | 199.99 | +--------------+----------+--------------+----------+--------+ 输出： +----------+----------------+-------------+------------------+--------------------+------------------+ | store_id | store_name | location | most_exp_product | cheapest_product | imbalance_ratio | +----------+----------------+-------------+------------------+--------------------+------------------+ | 3 | City Center | Los Angeles | Tablet | Stylus | 40.00 | | 1 | Downtown Tech | New York | Laptop | Mouse | 10.00 | | 2 | Suburb Mall | Chicago | Phone | Case | 25.00 | +----------+----------------+-------------+------------------+--------------------+------------------+ 解释： * Downtown Tech (store_id = 1)： * 最贵的商品：笔记本（$999.99）数量为 5 * 最便宜的商品：鼠标（$19.99）数量为 50 * 库存不平衡：5 < 50（贵的商品的库存更少） * 不平衡比：50 / 5 = 10.00 * 有 4 件商品（≥ 3），所以满足要求 * Suburb Mall (store_id = 2)： * 最贵的商品：手机（$699.99）数量为 3 * 最便宜的商品：保护壳（$15.99）数量为75 * 库存不平衡：3 < 75（贵的商品的库存更少） * 不平衡比：75 / 3 = 25.00 * 有 4 件商品（≥ 3），所以满足要求 * City Center (store_id = 3)： * 最贵的商品：平板电脑（$499.99）数量为 2 * 最便宜的商品：触控笔（$29.99）数量为 80 * 不平衡比：2 < 80（贵的商品的库存更少） * 不平衡比：80 / 2 = 40.00 * 有 3 件商品（≥ 3），所以满足要求 * 未包含的商店： * Corner Shop（store_id = 4）：只有两件商品（手表，手环）- 不满足最少 3 件商品的要求 * Plaza Store（store_id = 5）：只有两件商品（相机，镜头）- 不满足最少 3 件商品的要求 结果表按不平衡比降序排序，然后以商店名升序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 使用 Pandas 处理数据，首先合并 stores 和 inventory 表。
2. 计算每个商店的最贵商品和最便宜商品。
3. 计算不平衡比率，并过滤出至少有 3 个不同商品的商店。
4. 按不平衡比率降序和商店名称升序排序。

算法步骤:
1. 合并 stores 和 inventory 表。
2. 分组计算每个商店的最贵商品和最便宜商品。
3. 计算不平衡比率。
4. 过滤出至少有 3 个不同商品的商店。
5. 按不平衡比率降序和商店名称升序排序。

关键点:
- 使用 Pandas 的 groupby 和 agg 函数进行分组聚合。
- 使用 merge 函数合并表格。
- 使用 sort_values 函数进行排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 inventory 表的行数。主要的时间开销在于排序操作。
空间复杂度: O(n)，需要存储合并后的表格和中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd

def find_stores_with_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    # 合并 stores 和 inventory 表
    merged_df = pd.merge(inventory, stores, on='store_id')

    # 计算每个商店的最贵商品和最便宜商品
    exp_products = merged_df.groupby('store_id').apply(lambda x: x[x['price'] == x['price'].max()].sort_values(by='quantity', ascending=False).iloc[0])
    cheap_products = merged_df.groupby('store_id').apply(lambda x: x[x['price'] == x['price'].min()].sort_values(by='quantity', ascending=False).iloc[0])

    # 创建新的 DataFrame 来存储结果
    result = pd.DataFrame({
        'store_id': exp_products['store_id'],
        'store_name': exp_products['store_name'],
        'location': exp_products['location'],
        'most_exp_product': exp_products['product_name'],
        'cheapest_product': cheap_products['product_name'],
        'imbalance_ratio': (cheap_products['quantity'] / exp_products['quantity']).round(2)
    })

    # 过滤出至少有 3 个不同商品的商店
    store_counts = merged_df.groupby('store_id')['product_name'].nunique()
    result = result[result['store_id'].isin(store_counts[store_counts >= 3].index)]

    # 按不平衡比率降序和商店名称升序排序
    result = result.sort_values(by=['imbalance_ratio', 'store_name'], ascending=[False, True])

    return result

Solution = create_solution(find_stores_with_inventory_imbalance)