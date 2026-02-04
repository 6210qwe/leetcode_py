# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 607
标题: Sales Person
难度: easy
链接: https://leetcode.cn/problems/sales-person/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
607. 销售员 - 表: SalesPerson +-----------------+---------+ | Column Name | Type | +-----------------+---------+ | sales_id | int | | name | varchar | | salary | int | | commission_rate | int | | hire_date | date | +-----------------+---------+ sales_id 是该表的主键列(具有唯一值的列)。 该表的每一行都显示了销售人员的姓名和 ID ，以及他们的工资、佣金率和雇佣日期。 表: Company +-------------+---------+ | Column Name | Type | +-------------+---------+ | com_id | int | | name | varchar | | city | varchar | +-------------+---------+ com_id 是该表的主键列(具有唯一值的列)。 该表的每一行都表示公司的名称和 ID ，以及公司所在的城市。 表: Orders +-------------+------+ | Column Name | Type | +-------------+------+ | order_id | int | | order_date | date | | com_id | int | | sales_id | int | | amount | int | +-------------+------+ order_id 是该表的主键列(具有唯一值的列)。 com_id 是 Company 表中 com_id 的外键（reference 列）。 sales_id 是来自销售员表 sales_id 的外键（reference 列）。 该表的每一行包含一个订单的信息。这包括公司的 ID 、销售人员的 ID 、订单日期和支付的金额。 编写解决方案，找出没有任何与名为 “RED” 的公司相关的订单的所有销售人员的姓名。 以 任意顺序 返回结果表。 返回结果格式如下所示。 示例 1： 输入： SalesPerson 表: +----------+------+--------+-----------------+------------+ | sales_id | name | salary | commission_rate | hire_date | +----------+------+--------+-----------------+------------+ | 1 | John | 100000 | 6 | 4/1/2006 | | 2 | Amy | 12000 | 5 | 5/1/2010 | | 3 | Mark | 65000 | 12 | 12/25/2008 | | 4 | Pam | 25000 | 25 | 1/1/2005 | | 5 | Alex | 5000 | 10 | 2/3/2007 | +----------+------+--------+-----------------+------------+ Company 表: +--------+--------+----------+ | com_id | name | city | +--------+--------+----------+ | 1 | RED | Boston | | 2 | ORANGE | New York | | 3 | YELLOW | Boston | | 4 | GREEN | Austin | +--------+--------+----------+ Orders 表: +----------+------------+--------+----------+--------+ | order_id | order_date | com_id | sales_id | amount | +----------+------------+--------+----------+--------+ | 1 | 1/1/2014 | 3 | 4 | 10000 | | 2 | 2/1/2014 | 4 | 5 | 5000 | | 3 | 3/1/2014 | 1 | 1 | 50000 | | 4 | 4/1/2014 | 1 | 4 | 25000 | +----------+------------+--------+----------+--------+ 输出： +------+ | name | +------+ | Amy | | Mark | | Alex | +------+ 解释： 根据表 orders 中的订单 '3' 和 '4' ，容易看出只有 'John' 和 'Pam' 两个销售员曾经向公司 'RED' 销售过。 所以我们需要输出表 salesperson 中所有其他人的名字。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
1. 找出所有与 "RED" 公司相关的订单的 sales_id。
2. 从 SalesPerson 表中排除这些 sales_id，得到没有与 "RED" 公司相关订单的销售人员。

算法步骤:
1. 从 Company 表中找到 "RED" 公司的 com_id。
2. 从 Orders 表中找到与 "RED" 公司相关的所有订单的 sales_id。
3. 从 SalesPerson 表中排除这些 sales_id，得到最终结果。

关键点:
- 使用 SQL 查询来实现上述步骤。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 SalesPerson 表的大小，m 是 Orders 表的大小。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(sales_person: List[List[str]], company: List[List[str]], orders: List[List[str]]) -> List[str]:
    """
    函数式接口 - 找出没有任何与名为 “RED” 的公司相关的订单的所有销售人员的姓名。
    """
    # 从 Company 表中找到 "RED" 公司的 com_id
    red_com_id = None
    for com in company:
        if com[1] == "RED":
            red_com_id = com[0]
            break
    
    # 如果没有找到 "RED" 公司，直接返回所有销售人员的姓名
    if red_com_id is None:
        return [sp[1] for sp in sales_person]

    # 从 Orders 表中找到与 "RED" 公司相关的所有订单的 sales_id
    red_sales_ids = set()
    for order in orders:
        if order[2] == red_com_id:
            red_sales_ids.add(order[3])

    # 从 SalesPerson 表中排除这些 sales_id，得到最终结果
    result = []
    for sp in sales_person:
        if sp[0] not in red_sales_ids:
            result.append(sp[1])

    return result


Solution = create_solution(solution_function_name)