# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1541
标题: Top Travellers
难度: easy
链接: https://leetcode.cn/problems/top-travellers/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1407. 排名靠前的旅行者 - 表：Users +---------------+---------+ | Column Name | Type | +---------------+---------+ | id | int | | name | varchar | +---------------+---------+ id 是该表中具有唯一值的列。 name 是用户名字。 表：Rides +---------------+---------+ | Column Name | Type | +---------------+---------+ | id | int | | user_id | int | | distance | int | +---------------+---------+ id 是该表中具有唯一值的列。 user_id 是本次行程的用户的 id, 而该用户此次行程距离为 distance 。 编写解决方案，报告每个用户的旅行距离。 返回的结果表单，以 travelled_distance 降序排列 ，如果有两个或者更多的用户旅行了相同的距离, 那么再以 name 升序排列 。 返回结果格式如下例所示。 示例 1： 输入： Users 表： +------+-----------+ | id | name | +------+-----------+ | 1 | Alice | | 2 | Bob | | 3 | Alex | | 4 | Donald | | 7 | Lee | | 13 | Jonathan | | 19 | Elvis | +------+-----------+ Rides 表： +------+----------+----------+ | id | user_id | distance | +------+----------+----------+ | 1 | 1 | 120 | | 2 | 2 | 317 | | 3 | 3 | 222 | | 4 | 7 | 100 | | 5 | 13 | 312 | | 6 | 19 | 50 | | 7 | 7 | 120 | | 8 | 19 | 400 | | 9 | 7 | 230 | +------+----------+----------+ 输出： +----------+--------------------+ | name | travelled_distance | +----------+--------------------+ | Elvis | 450 | | Lee | 450 | | Bob | 317 | | Jonathan | 312 | | Alex | 222 | | Alice | 120 | | Donald | 0 | +----------+--------------------+ 解释： Elvis 和 Lee 旅行了 450 英里，Elvis 是排名靠前的旅行者，因为他的名字在字母表上的排序比 Lee 更小。 Bob, Jonathan, Alex 和 Alice 只有一次行程，我们只按此次行程的全部距离对他们排序。 Donald 没有任何行程, 他的旅行距离为 0。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个用户的总旅行距离，并按要求排序。

算法步骤:
1. 将 Users 表和 Rides 表进行左连接，以获取每个用户的旅行记录。
2. 使用 GROUP BY 对用户进行分组，并使用 SUM 函数计算每个用户的总旅行距离。
3. 使用 COALESCE 函数将没有旅行记录的用户的旅行距离设为 0。
4. 按 travelled_distance 降序排列，如果 travel_distance 相同，则按 name 升序排列。

关键点:
- 使用 LEFT JOIN 确保所有用户都包含在结果中，即使他们没有旅行记录。
- 使用 COALESCE 处理 NULL 值，确保没有旅行记录的用户显示为 0。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是用户的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(1)，查询的空间复杂度主要取决于数据库的内部实现，但通常为常数级别。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(users: List[List[str]], rides: List[List[int]]) -> List[List[str]]:
    """
    函数式接口 - 实现最优解法
    """
    # 创建一个字典来存储每个用户的总旅行距离
    user_distances = {}
    
    # 遍历 rides 表，计算每个用户的总旅行距离
    for ride in rides:
        user_id, distance = ride[1], ride[2]
        if user_id in user_distances:
            user_distances[user_id] += distance
        else:
            user_distances[user_id] = distance
    
    # 创建结果列表
    result = []
    
    # 遍历 users 表，生成结果
    for user in users:
        user_id, name = int(user[0]), user[1]
        travelled_distance = user_distances.get(user_id, 0)
        result.append([name, travelled_distance])
    
    # 按 travelled_distance 降序排列，如果 travel_distance 相同，则按 name 升序排列
    result.sort(key=lambda x: (-x[1], x[0]))
    
    return result


Solution = create_solution(solution_function_name)