# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1338
标题: Queries Quality and Percentage
难度: easy
链接: https://leetcode.cn/problems/queries-quality-and-percentage/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1211. 查询结果的质量和占比 - Queries 表： +-------------+---------+ | Column Name | Type | +-------------+---------+ | query_name | varchar | | result | varchar | | position | int | | rating | int | +-------------+---------+ 此表可能有重复的行。 此表包含了一些从数据库中收集的查询信息。 “位置”（position）列的值为 1 到 500 。 “评分”（rating）列的值为 1 到 5 。评分小于 3 的查询被定义为质量很差的查询。 将查询结果的质量 quality 定义为： > 各查询结果的评分与其位置之间比率的平均值。 将劣质查询百分比 poor_query_percentage 定义为： > 评分小于 3 的查询结果占全部查询结果的百分比。 编写解决方案，找出每次的 query_name 、 quality 和 poor_query_percentage。 quality 和 poor_query_percentage 都应 四舍五入到小数点后两位 。 以 任意顺序 返回结果表。 结果格式如下所示： 示例 1： 输入： Queries table: +------------+-------------------+----------+--------+ | query_name | result | position | rating | +------------+-------------------+----------+--------+ | Dog | Golden Retriever | 1 | 5 | | Dog | German Shepherd | 2 | 5 | | Dog | Mule | 200 | 1 | | Cat | Shirazi | 5 | 2 | | Cat | Siamese | 3 | 3 | | Cat | Sphynx | 7 | 4 | +------------+-------------------+----------+--------+ 输出： +------------+---------+-----------------------+ | query_name | quality | poor_query_percentage | +------------+---------+-----------------------+ | Dog | 2.50 | 33.33 | | Cat | 0.66 | 33.33 | +------------+---------+-----------------------+ 解释： Dog 查询结果的质量为 ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50 Dog 查询结果的劣质查询百分比为 (1 / 3) * 100 = 33.33 Cat 查询结果的质量为 ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66 Cat 查询结果的劣质查询百分比为 (1 / 3) * 100 = 33.33
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Pandas 库进行数据处理和计算。

算法步骤:
1. 计算每个查询的 quality。
2. 计算每个查询的 poor_query_percentage。
3. 合并结果并四舍五入到小数点后两位。

关键点:
- 使用 Pandas 库进行高效的数据处理。
- 使用 groupby 和 agg 方法进行分组聚合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd


def solution(queries: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 计算每个查询的 quality 和 poor_query_percentage
    """
    # 计算每个查询的 quality
    queries['quality'] = queries['rating'] / queries['position']
    quality_df = queries.groupby('query_name')['quality'].mean().reset_index()

    # 计算每个查询的 poor_query_percentage
    poor_queries = queries[queries['rating'] < 3]
    poor_query_count = poor_queries.groupby('query_name').size()
    total_query_count = queries.groupby('query_name').size()
    poor_query_percentage = (poor_query_count / total_query_count * 100).round(2).reset_index(name='poor_query_percentage')

    # 合并结果
    result = pd.merge(quality_df, poor_query_percentage, on='query_name')
    result['quality'] = result['quality'].round(2)

    return result


Solution = create_solution(solution)