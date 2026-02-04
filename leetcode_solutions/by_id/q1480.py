# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1480
标题: Movie Rating
难度: medium
链接: https://leetcode.cn/problems/movie-rating/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1341. 电影评分 - 表：Movies +---------------+---------+ | Column Name | Type | +---------------+---------+ | movie_id | int | | title | varchar | +---------------+---------+ movie_id 是这个表的主键(具有唯一值的列)。 title 是电影的名字。 每部电影都有一个唯一的 title。 表：Users +---------------+---------+ | Column Name | Type | +---------------+---------+ | user_id | int | | name | varchar | +---------------+---------+ user_id 是表的主键(具有唯一值的列)。 'name' 列具有唯一值。 表：MovieRating +---------------+---------+ | Column Name | Type | +---------------+---------+ | movie_id | int | | user_id | int | | rating | int | | created_at | date | +---------------+---------+ (movie_id, user_id) 是这个表的主键(具有唯一值的列的组合)。 这个表包含用户在其评论中对电影的评分 rating 。 created_at 是用户的点评日期。 请你编写一个解决方案： * 查找评论电影数量最多的用户名。如果出现平局，返回字典序较小的用户名。 * 查找在 February 2020 平均评分最高 的电影名称。如果出现平局，返回字典序较小的电影名称。 字典序 ，即按字母在字典中出现顺序对字符串排序，字典序较小则意味着排序靠前。 返回结果格式如下例所示。 示例 1： 输入： Movies 表： +-------------+--------------+ | movie_id | title | +-------------+--------------+ | 1 | Avengers | | 2 | Frozen 2 | | 3 | Joker | +-------------+--------------+ Users 表： +-------------+--------------+ | user_id | name | +-------------+--------------+ | 1 | Daniel | | 2 | Monica | | 3 | Maria | | 4 | James | +-------------+--------------+ MovieRating 表： +-------------+--------------+--------------+-------------+ | movie_id | user_id | rating | created_at | +-------------+--------------+--------------+-------------+ | 1 | 1 | 3 | 2020-01-12 | | 1 | 2 | 4 | 2020-02-11 | | 1 | 3 | 2 | 2020-02-12 | | 1 | 4 | 1 | 2020-01-01 | | 2 | 1 | 5 | 2020-02-17 | | 2 | 2 | 2 | 2020-02-01 | | 2 | 3 | 2 | 2020-03-01 | | 3 | 1 | 3 | 2020-02-22 | | 3 | 2 | 4 | 2020-02-25 | +-------------+--------------+--------------+-------------+ 输出： Result 表： +--------------+ | results | +--------------+ | Daniel | | Frozen 2 | +--------------+ 解释： Daniel 和 Monica 都点评了 3 部电影（"Avengers", "Frozen 2" 和 "Joker"） 但是 Daniel 字典序比较小。 Frozen 2 和 Joker 在 2 月的评分都是 3.5，但是 Frozen 2 的字典序比较小。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 使用子查询和聚合函数来找到评论电影数量最多的用户名。
2. 使用子查询和聚合函数来找到在 February 2020 平均评分最高的电影名称。

算法步骤:
1. 找到评论电影数量最多的用户名：
   - 计算每个用户评论的电影数量。
   - 按评论数量降序排序，取第一个用户。
   - 如果有多个用户评论数量相同，按用户名字典序排序取第一个。
2. 找到在 February 2020 平均评分最高的电影名称：
   - 过滤出在 February 2020 的评分记录。
   - 计算每部电影的平均评分。
   - 按平均评分降序排序，取第一个电影。
   - 如果有多部电影平均评分相同，按电影名字典序排序取第一个。

关键点:
- 使用 SQL 子查询和聚合函数来实现高效的查询。
- 确保在处理平局时按字典序排序。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 MovieRating 表中的记录数。主要的时间开销在于排序操作。
空间复杂度: O(1)，不使用额外的空间，只使用常数级的变量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(movies, users, movie_rating):
    """
    函数式接口 - 实现
    """
    # 查询评论电影数量最多的用户名
    user_query = """
    SELECT u.name
    FROM (
        SELECT user_id, COUNT(movie_id) AS review_count
        FROM movie_rating
        GROUP BY user_id
        ORDER BY review_count DESC, u.name ASC
        LIMIT 1
    ) AS subquery
    JOIN users u ON subquery.user_id = u.user_id
    """

    # 查询在 February 2020 平均评分最高的电影名称
    movie_query = """
    SELECT m.title
    FROM (
        SELECT movie_id, AVG(rating) AS avg_rating
        FROM movie_rating
        WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
        GROUP BY movie_id
        ORDER BY avg_rating DESC, m.title ASC
        LIMIT 1
    ) AS subquery
    JOIN movies m ON subquery.movie_id = m.movie_id
    """

    # 执行查询
    user_result = users.execute(user_query).fetchone()[0]
    movie_result = movies.execute(movie_query).fetchone()[0]

    return [user_result, movie_result]

Solution = create_solution(solution_function_name)