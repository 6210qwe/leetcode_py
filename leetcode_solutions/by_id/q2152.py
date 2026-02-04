# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2152
标题: The Number of Seniors and Juniors to Join the Company
难度: hard
链接: https://leetcode.cn/problems/the-number-of-seniors-and-juniors-to-join-the-company/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2004. 职员招聘人数 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来统计满足条件的高级职员和初级职员的数量。

算法步骤:
1. 创建一个子查询来计算每个部门的总招聘人数。
2. 使用主查询来过滤出满足条件的高级职员和初级职员，并进行统计。

关键点:
- 使用子查询来简化主查询的条件判断。
- 确保查询的性能优化，避免不必要的全表扫描。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是员工表的行数。因为我们需要遍历整个表来计算每个部门的总招聘人数。
空间复杂度: O(1)，因为我们只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

def solution_function_name(params):
    """
    函数式接口 - 使用 SQL 查询来统计满足条件的高级职员和初级职员的数量
    """
    # SQL 查询实现
    query = """
    WITH TotalHires AS (
        SELECT department_id, COUNT(*) AS total_hires
        FROM Employees
        GROUP BY department_id
    )
    SELECT 
        SUM(CASE WHEN experience = 'Senior' THEN 1 ELSE 0 END) AS senior_count,
        SUM(CASE WHEN experience = 'Junior' THEN 1 ELSE 0 END) AS junior_count
    FROM Employees
    WHERE (experience = 'Senior' AND salary <= (SELECT MAX(salary) FROM Employees WHERE department_id = Employees.department_id))
      OR (experience = 'Junior' AND salary <= (SELECT 0.75 * MAX(salary) FROM Employees WHERE department_id = Employees.department_id))
    """

    # 返回查询结果
    return query


Solution = create_solution(solution_function_name)