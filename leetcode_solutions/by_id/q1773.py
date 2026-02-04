# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1773
标题: Percentage of Users Attended a Contest
难度: easy
链接: https://leetcode.cn/problems/percentage-of-users-attended-a-contest/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1633. 各赛事的用户注册率 - 用户表： Users +-------------+---------+ | Column Name | Type | +-------------+---------+ | user_id | int | | user_name | varchar | +-------------+---------+ user_id 是该表的主键(具有唯一值的列)。 该表中的每行包括用户 ID 和用户名。 注册表： Register +-------------+---------+ | Column Name | Type | +-------------+---------+ | contest_id | int | | user_id | int | +-------------+---------+ (contest_id, user_id) 是该表的主键(具有唯一值的列的组合)。 该表中的每行包含用户的 ID 和他们注册的赛事。 编写解决方案统计出各赛事的用户注册百分率，保留两位小数。 返回的结果表按 percentage 的 降序 排序，若相同则按 contest_id 的 升序 排序。 返回结果如下示例所示。 示例 1： 输入： Users 表： +---------+-----------+ | user_id | user_name | +---------+-----------+ | 6 | Alice | | 2 | Bob | | 7 | Alex | +---------+-----------+ Register 表： +------------+---------+ | contest_id | user_id | +------------+---------+ | 215 | 6 | | 209 | 2 | | 208 | 2 | | 210 | 6 | | 208 | 6 | | 209 | 7 | | 209 | 6 | | 215 | 7 | | 208 | 7 | | 210 | 2 | | 207 | 2 | | 210 | 7 | +------------+---------+ 输出： +------------+------------+ | contest_id | percentage | +------------+------------+ | 208 | 100.0 | | 209 | 100.0 | | 210 | 100.0 | | 215 | 66.67 | | 207 | 33.33 | +------------+------------+ 解释： 所有用户都注册了 208、209 和 210 赛事，因此这些赛事的注册率为 100% ，我们按 contest_id 的降序排序加入结果表中。 Alice 和 Alex 注册了 215 赛事，注册率为 ((2/3) * 100) = 66.67% Bob 注册了 207 赛事，注册率为 ((1/3) * 100) = 33.33%
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 SQL 查询来计算每个赛事的注册百分比，并按要求排序。

算法步骤:
1. 计算总用户数。
2. 统计每个赛事的注册用户数。
3. 计算每个赛事的注册百分比。
4. 按注册百分比降序和赛事ID升序排序。

关键点:
- 使用子查询来获取总用户数。
- 使用 COUNT 和 GROUP BY 来统计每个赛事的注册用户数。
- 使用 ROUND 函数来保留两位小数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是注册表的行数。主要开销在排序操作上。
空间复杂度: O(n)，存储中间结果和最终结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(users: List[List[int]], register: List[List[int]]) -> List[List[float]]:
    """
    函数式接口 - 计算各赛事的用户注册百分比
    """
    from collections import defaultdict
    import pandas as pd

    # 将输入转换为 DataFrame
    users_df = pd.DataFrame(users, columns=['user_id', 'user_name'])
    register_df = pd.DataFrame(register, columns=['contest_id', 'user_id'])

    # 计算总用户数
    total_users = len(users_df)

    # 统计每个赛事的注册用户数
    contest_counts = register_df.groupby('contest_id').size().reset_index(name='count')

    # 计算每个赛事的注册百分比
    contest_counts['percentage'] = (contest_counts['count'] / total_users * 100).round(2)

    # 按注册百分比降序和赛事ID升序排序
    result = contest_counts.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])

    # 返回结果
    return result[['contest_id', 'percentage']].values.tolist()


Solution = create_solution(solution_function_name)