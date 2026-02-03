# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 175
标题: Combine Two Tables
难度: easy
链接: https://leetcode.cn/problems/combine-two-tables/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
175. 组合两个表 - 表: Person +-------------+---------+ | 列名 | 类型 | +-------------+---------+ | PersonId | int | | FirstName | varchar | | LastName | varchar | +-------------+---------+ personId 是该表的主键（具有唯一值的列）。 该表包含一些人的 ID 和他们的姓和名的信息。 表: Address +-------------+---------+ | 列名 | 类型 | +-------------+---------+ | AddressId | int | | PersonId | int | | City | varchar | | State | varchar | +-------------+---------+ addressId 是该表的主键（具有唯一值的列）。 该表的每一行都包含一个 ID = PersonId 的人的城市和州的信息。 编写解决方案，报告 Person 表中每个人的姓、名、城市和州。如果 personId 的地址不在 Address 表中，则报告为 null 。 以 任意顺序 返回结果表。 结果格式如下所示。 示例 1: 输入: Person表: +----------+----------+-----------+ | personId | lastName | firstName | +----------+----------+-----------+ | 1 | Wang | Allen | | 2 | Alice | Bob | +----------+----------+-----------+ Address表: +-----------+----------+---------------+------------+ | addressId | personId | city | state | +-----------+----------+---------------+------------+ | 1 | 2 | New York City | New York | | 2 | 3 | Leetcode | California | +-----------+----------+---------------+------------+ 输出: +-----------+----------+---------------+----------+ | firstName | lastName | city | state | +-----------+----------+---------------+----------+ | Allen | Wang | Null | Null | | Bob | Alice | New York City | New York | +-----------+----------+---------------+----------+ 解释: 地址表中没有 personId = 1 的地址，所以它们的城市和州返回 null。 addressId = 1 包含了 personId = 2 的地址信息。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: SQL LEFT JOIN查询，保留Person表的所有记录

算法步骤:
1. 使用LEFT JOIN连接Person和Address表
2. 以Person.personId = Address.personId为连接条件
3. 选择firstName, lastName, city, state字段

关键点:
- 使用LEFT JOIN保留Person表的所有记录
- SQL查询语句
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n+m) - n和m分别是两个表的记录数
空间复杂度: O(n+m) - 连接结果的空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from leetcode_solutions.utils.solution import create_solution


def combine_two_tables():
    """
    函数式接口 - 组合两个表（SQL查询）
    
    实现思路:
    使用LEFT JOIN连接Person和Address表，保留Person表的所有记录。
    
    Returns:
        SQL查询语句字符串
        
    Example:
        >>> sql = combine_two_tables()
        >>> # 执行SQL查询
    """
    sql = """
    SELECT p.firstName, p.lastName, a.city, a.state
    FROM Person p
    LEFT JOIN Address a ON p.personId = a.personId
    """
    return sql.strip()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(combine_two_tables)
