# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3921
标题: Find Consistently Improving Employees
难度: medium
链接: https://leetcode.cn/problems/find-consistently-improving-employees/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3580. 寻找持续进步的员工 - 表：employees +-------------+---------+ | Column Name | Type | +-------------+---------+ | employee_id | int | | name | varchar | +-------------+---------+ employee_id 是这张表的唯一主键。 每一行包含一名员工的信息。 表：performance_reviews +-------------+------+ | Column Name | Type | +-------------+------+ | review_id | int | | employee_id | int | | review_date | date | | rating | int | +-------------+------+ review_id 是这张表的唯一主键。 每一行表示一名员工的绩效评估。评分在 1-5 的范围内，5分代表优秀，1分代表较差。 编写一个解决方案，以找到在过去三次评估中持续提高绩效的员工。 * 员工 至少需要 3 次评估 才能被考虑 * 员工过去的 3 次评估，评分必须 严格递增（每次评价都比上一次好） * 根据 review_date 为每位员工分析最近的 3 次评估 * 进步分数 为最后 3 次评估中最后一次评分与最早一次评分之间的差值 返回结果表以 进步分数 降序 排序，然后以 名字 升序 排序。 结果格式如下所示。 示例： 输入： employees 表： +-------------+----------------+ | employee_id | name | +-------------+----------------+ | 1 | Alice Johnson | | 2 | Bob Smith | | 3 | Carol Davis | | 4 | David Wilson | | 5 | Emma Brown | +-------------+----------------+ performance_reviews 表： +-----------+-------------+-------------+--------+ | review_id | employee_id | review_date | rating | +-----------+-------------+-------------+--------+ | 1 | 1 | 2023-01-15 | 2 | | 2 | 1 | 2023-04-15 | 3 | | 3 | 1 | 2023-07-15 | 4 | | 4 | 1 | 2023-10-15 | 5 | | 5 | 2 | 2023-02-01 | 3 | | 6 | 2 | 2023-05-01 | 2 | | 7 | 2 | 2023-08-01 | 4 | | 8 | 2 | 2023-11-01 | 5 | | 9 | 3 | 2023-03-10 | 1 | | 10 | 3 | 2023-06-10 | 2 | | 11 | 3 | 2023-09-10 | 3 | | 12 | 3 | 2023-12-10 | 4 | | 13 | 4 | 2023-01-20 | 4 | | 14 | 4 | 2023-04-20 | 4 | | 15 | 4 | 2023-07-20 | 4 | | 16 | 5 | 2023-02-15 | 3 | | 17 | 5 | 2023-05-15 | 2 | +-----------+-------------+-------------+--------+ 输出： +-------------+----------------+-------------------+ | employee_id | name | improvement_score | +-------------+----------------+-------------------+ | 2 | Bob Smith | 3 | | 1 | Alice Johnson | 2 | | 3 | Carol Davis | 2 | +-------------+----------------+-------------------+ 解释： * Alice Johnson (employee_id = 1)： * 有 4 次评估，分数：2, 3, 4, 5 * 最后 3 次评估（按日期）：2023-04-15 (3), 2023-07-15 (4), 2023-10-15 (5) * 评分严格递增：3 → 4 → 5 * 进步分数：5 - 3 = 2 * Carol Davis (employee_id = 3)： * 有 4 次评估，分数：1, 2, 3, 4 * 最后 3 次评估（按日期）：2023-06-10 (2)，2023-09-10 (3)，2023-12-10 (4) * 评分严格递增：2 → 3 → 4 * 进步分数：4 - 2 = 2 * Bob Smith (employee_id = 2)： * 有 4 次评估，分数：3，2，4，5 * 最后 3 次评估（按日期）：2023-05-01 (2)，2023-08-01 (4)，2023-11-01 (5) * 评分严格递增：2 → 4 → 5 * 进步分数：5 - 2 = 3 * 未包含的员工： * David Wilson (employee_id = 4)：之前 3 次评估都是 4 分（没有进步） * Emma Brown (employee_id = 5)：只有 2 次评估（需要至少 3 次） 输出表以 improvement_score 降序排序，然后以 name 升序排序。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用 SQL 查询来筛选出每个员工的最近三次评估，并检查这些评估是否严格递增。
- 计算进步分数，并根据进步分数和名字进行排序。

算法步骤:
1. 从 `performance_reviews` 表中选择每个员工的最近三次评估。
2. 检查这些评估是否严格递增。
3. 计算进步分数（最后一次评分减去第一次评分）。
4. 将结果与 `employees` 表连接，获取员工的名字。
5. 根据进步分数降序和名字升序排序。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 来获取每个员工的最近三次评估。
- 使用 `LAG()` 函数来检查评分是否严格递增。
- 使用 `CASE` 语句来计算进步分数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是 `performance_reviews` 表中的行数。主要的时间消耗在于排序操作。
空间复杂度: O(n)，用于存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name(employees, performance_reviews):
    """
    函数式接口 - 实现
    """
    # 使用 SQL 查询来实现
    query = """
    WITH RecentReviews AS (
        SELECT
            pr.employee_id,
            pr.review_date,
            pr.rating,
            ROW_NUMBER() OVER (PARTITION BY pr.employee_id ORDER BY pr.review_date DESC) AS rn
        FROM
            performance_reviews pr
    ),
    FilteredReviews AS (
        SELECT
            rr.employee_id,
            rr.review_date,
            rr.rating,
            LAG(rr.rating, 1) OVER (PARTITION BY rr.employee_id ORDER BY rr.review_date) AS prev_rating,
            LAG(rr.rating, 2) OVER (PARTITION BY rr.employee_id ORDER BY rr.review_date) AS prev_prev_rating
        FROM
            RecentReviews rr
        WHERE
            rr.rn <= 3
    ),
    ImprovedEmployees AS (
        SELECT
            fr.employee_id,
            MAX(fr.rating) - MIN(fr.rating) AS improvement_score
        FROM
            FilteredReviews fr
        GROUP BY
            fr.employee_id
        HAVING
            COUNT(fr.employee_id) = 3 AND
            SUM(CASE WHEN fr.rating > fr.prev_rating THEN 1 ELSE 0 END) = 2 AND
            SUM(CASE WHEN fr.prev_rating > fr.prev_prev_rating THEN 1 ELSE 0 END) = 1
    )
    SELECT
        e.employee_id,
        e.name,
        ie.improvement_score
    FROM
        ImprovedEmployees ie
    JOIN
        employees e ON ie.employee_id = e.employee_id
    ORDER BY
        ie.improvement_score DESC,
        e.name ASC;
    """
    return query


Solution = create_solution(solution_function_name)