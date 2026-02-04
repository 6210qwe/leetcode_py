# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3996
标题: Find Books with Polarized Opinions
难度: medium
链接: https://leetcode.cn/problems/find-books-with-polarized-opinions/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3642. 查找有两极分化观点的书籍 - 表：books +-------------+---------+ | Column Name | Type | +-------------+---------+ | book_id | int | | title | varchar | | author | varchar | | genre | varchar | | pages | int | +-------------+---------+ book_id 是这张表的唯一主键。 每一行包含关于一本书的信息，包括其类型和页数。 表：reading_sessions +----------------+---------+ | Column Name | Type | +----------------+---------+ | session_id | int | | book_id | int | | reader_name | varchar | | pages_read | int | | session_rating | int | +----------------+---------+ session_id 是这张表的唯一主键。 每一行代表一次阅读事件，有人阅读了书籍的一部分。session_rating 在 1-5 的范围内。 编写一个解决方案来找到具有 两极分化观点 的书 - 同时获得不同读者极高和极低评分的书籍。 * 如果一本书有至少一个大于等于 4 的评分和至少一个小于等于 2 的评分则是有两极分化观点的书 * 只考虑有至少 5 次阅读事件的书籍 * 按 highest_rating - lowest_rating 计算评分差幅 rating spread * 按极端评分（评分小于等于 2 或大于等于 4）的数量除以总阅读事件计算 极化得分 polarization score * 只包含 极化得分大于等于 0.6 的书（至少 60% 极端评分） 返回结果表按极化得分 降序 排序，然后按标题 降序 排序。 极化得分应舍入到 2 位小数。 返回格式如下所示。 示例： 输入： books 表： +---------+------------------------+---------------+----------+-------+ | book_id | title | author | genre | pages | +---------+------------------------+---------------+----------+-------+ | 1 | The Great Gatsby | F. Scott | Fiction | 180 | | 2 | To Kill a Mockingbird | Harper Lee | Fiction | 281 | | 3 | 1984 | George Orwell | Dystopian| 328 | | 4 | Pride and Prejudice | Jane Austen | Romance | 432 | | 5 | The Catcher in the Rye | J.D. Salinger | Fiction | 277 | +---------+------------------------+---------------+----------+-------+ reading_sessions 表： +------------+---------+-------------+------------+----------------+ | session_id | book_id | reader_name | pages_read | session_rating | +------------+---------+-------------+------------+----------------+ | 1 | 1 | Alice | 50 | 5 | | 2 | 1 | Bob | 60 | 1 | | 3 | 1 | Carol | 40 | 4 | | 4 | 1 | David | 30 | 2 | | 5 | 1 | Emma | 45 | 5 | | 6 | 2 | Frank | 80 | 4 | | 7 | 2 | Grace | 70 | 4 | | 8 | 2 | Henry | 90 | 5 | | 9 | 2 | Ivy | 60 | 4 | | 10 | 2 | Jack | 75 | 4 | | 11 | 3 | Kate | 100 | 2 | | 12 | 3 | Liam | 120 | 1 | | 13 | 3 | Mia | 80 | 2 | | 14 | 3 | Noah | 90 | 1 | | 15 | 3 | Olivia | 110 | 4 | | 16 | 3 | Paul | 95 | 5 | | 17 | 4 | Quinn | 150 | 3 | | 18 | 4 | Ruby | 140 | 3 | | 19 | 5 | Sam | 80 | 1 | | 20 | 5 | Tara | 70 | 2 | +------------+---------+-------------+------------+----------------+ 输出： +---------+------------------+---------------+-----------+-------+---------------+--------------------+ | book_id | title | author | genre | pages | rating_spread | polarization_score | +---------+------------------+---------------+-----------+-------+---------------+--------------------+ | 1 | The Great Gatsby | F. Scott | Fiction | 180 | 4 | 1.00 | | 3 | 1984 | George Orwell | Dystopian | 328 | 4 | 1.00 | +---------+------------------+---------------+-----------+-------+---------------+--------------------+ 解释： * 了不起的盖茨比（book_id = 1）： * 有 5 次阅读事件（满足最少要求） * 评分：5, 1, 4, 2, 5 * 大于等于 4 的评分：5，4，5（3 次事件） * 小于等于 2 的评分：1，2（2 次事件） * 评分差：5 - 1 = 4 * 极端评分（≤2 或 ≥4）：所有 5 次事件（5，1，4，2，5） * 极化得分：5/5 = 1.00（≥ 0.6，符合） * 1984 (book_id = 3): * 有 6 次阅读事件（满足最少要求） * 评分：2，1，2，1，4，5 * 大于等于 4 的评分：4，5（2 次事件） * 小于等于 2 的评分：2，1，2，1（4 次事件） * 评分差：5 - 1 = 4 * 极端评分（≤2 或 ≥4）：所有 6 次事件（2，1，2，1，4，5） * 极化得分：6/6 = 1.00 (≥ 0.6，符合） * 未包含的书： * 杀死一只知更鸟（book_id = 2）：所有评分为 4-5，没有低分（≤2） * 傲慢与偏见（book_id = 4）：只有 2 次事件（< 最少 5 次） * 麦田里的守望者（book_id = 5）：只有 2 次事件（< 最少 5 次） 结果表按极化得分降序排序，然后按标题降序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Pandas 进行数据处理，通过聚合和筛选找到符合条件的书籍。

算法步骤:
1. 合并 `books` 和 `reading_sessions` 表，基于 `book_id`。
2. 筛选出至少有 5 次阅读事件的书籍。
3. 计算每本书的最高评分、最低评分和评分差幅。
4. 计算每本书的极端评分数量和总评分数量。
5. 计算极化得分，并筛选出极化得分大于等于 0.6 的书籍。
6. 按极化得分降序排序，然后按标题降序排序。

关键点:
- 使用 Pandas 的 `merge` 和 `groupby` 方法进行数据处理。
- 使用条件筛选和聚合函数计算所需的统计值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `reading_sessions` 表的长度。主要的时间开销在于排序操作。
空间复杂度: O(n)，需要存储合并后的数据表。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd

def find_books_with_polarized_opinions(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    # 合并 books 和 reading_sessions 表
    merged_df = pd.merge(books, reading_sessions, on='book_id', how='left')
    
    # 筛选出至少有 5 次阅读事件的书籍
    filtered_df = merged_df.groupby('book_id').filter(lambda x: len(x) >= 5)
    
    # 计算每本书的最高评分、最低评分和评分差幅
    agg_df = filtered_df.groupby('book_id').agg(
        highest_rating=('session_rating', 'max'),
        lowest_rating=('session_rating', 'min'),
        total_sessions=('session_rating', 'count')
    ).reset_index()
    
    # 计算评分差幅
    agg_df['rating_spread'] = agg_df['highest_rating'] - agg_df['lowest_rating']
    
    # 计算极端评分数量
    extreme_ratings = filtered_df[filtered_df['session_rating'].isin([1, 2, 4, 5])]
    extreme_counts = extreme_ratings.groupby('book_id')['session_rating'].count().reset_index(name='extreme_count')
    
    # 合并极端评分数量
    final_df = pd.merge(agg_df, extreme_counts, on='book_id', how='left')
    
    # 计算极化得分
    final_df['polarization_score'] = (final_df['extreme_count'] / final_df['total_sessions']).round(2)
    
    # 筛选出极化得分大于等于 0.6 的书籍
    result_df = final_df[final_df['polarization_score'] >= 0.6]
    
    # 合并书籍详细信息
    result_df = pd.merge(result_df, books, on='book_id', how='left')
    
    # 按极化得分降序排序，然后按标题降序排序
    result_df = result_df.sort_values(by=['polarization_score', 'title'], ascending=[False, False])
    
    # 选择输出列
    result_df = result_df[['book_id', 'title', 'author', 'genre', 'pages', 'rating_spread', 'polarization_score']]
    
    return result_df

Solution = create_solution(find_books_with_polarized_opinions)