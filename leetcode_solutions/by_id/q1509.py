# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1509
标题: Replace Employee ID With The Unique Identifier
难度: easy
链接: https://leetcode.cn/problems/replace-employee-id-with-the-unique-identifier/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1378. 使用唯一标识码替换员工ID - Employees 表： +---------------+---------+ | Column Name | Type | +---------------+---------+ | id | int | | name | varchar | +---------------+---------+ 在 SQL 中，id 是这张表的主键。 这张表的每一行分别代表了某公司其中一位员工的名字和 ID 。 EmployeeUNI 表： +---------------+---------+ | Column Name | Type | +---------------+---------+ | id | int | | unique_id | int | +---------------+---------+ 在 SQL 中，(id, unique_id) 是这张表的主键。 这张表的每一行包含了该公司某位员工的 ID 和他的唯一标识码（unique ID）。 展示每位用户的 唯一标识码（unique ID ）；如果某位员工没有唯一标识码，使用 null 填充即可。 你可以以 任意 顺序返回结果表。 返回结果的格式如下例所示。 示例 1： 输入： Employees 表: +----+----------+ | id | name | +----+----------+ | 1 | Alice | | 7 | Bob | | 11 | Meir | | 90 | Winston | | 3 | Jonathan | +----+----------+ EmployeeUNI 表: +----+-----------+ | id | unique_id | +----+-----------+ | 3 | 1 | | 11 | 2 | | 90 | 3 | +----+-----------+ 输出： +-----------+----------+ | unique_id | name | +-----------+----------+ | null | Alice | | null | Bob | | 2 | Meir | | 3 | Winston | | 1 | Jonathan | +-----------+----------+ 解释： Alice and Bob 没有唯一标识碼, 因此我们使用 null 替代。 Meir 的唯一标识碼是 2 。 Winston 的唯一标识碼是 3 。 Jonathan 唯一标识碼是 1 。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来存储 EmployeeUNI 表中的 unique_id 和 id 的映射关系，然后遍历 Employees 表，将每个员工的 id 替换为对应的 unique_id。

算法步骤:
1. 创建一个哈希表 `id_to_unique_id`，用于存储 EmployeeUNI 表中的 id 和 unique_id 的映射关系。
2. 遍历 EmployeeUNI 表，将每个 id 和对应的 unique_id 存入哈希表 `id_to_unique_id`。
3. 遍历 Employees 表，对于每个员工，从哈希表 `id_to_unique_id` 中获取其对应的 unique_id，如果不存在则使用 null。
4. 返回包含 unique_id 和 name 的结果列表。

关键点:
- 使用哈希表可以实现 O(1) 时间复杂度的查找操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 Employees 表的长度，m 是 EmployeeUNI 表的长度。
空间复杂度: O(m)，需要额外的空间来存储 EmployeeUNI 表中的 id 和 unique_id 的映射关系。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def replace_employee_id_with_unique_identifier(employees: List[List[int]], employee_uni: List[List[int]]) -> List[List[Optional[int]]]:
    """
    函数式接口 - 将员工 ID 替换为唯一标识码
    """
    # 创建一个哈希表来存储 EmployeeUNI 表中的 id 和 unique_id 的映射关系
    id_to_unique_id = {uni_id: unique_id for uni_id, unique_id in employee_uni}
    
    # 遍历 Employees 表，将每个员工的 id 替换为对应的 unique_id
    result = []
    for emp_id, name in employees:
        unique_id = id_to_unique_id.get(emp_id, None)
        result.append([unique_id, name])
    
    return result


Solution = create_solution(replace_employee_id_with_unique_identifier)