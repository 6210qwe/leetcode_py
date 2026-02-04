# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2087
标题: Confirmation Rate
难度: medium
链接: https://leetcode.cn/problems/confirmation-rate/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1934. 确认率 - 表: Signups +----------------+----------+ | Column Name | Type | +----------------+----------+ | user_id | int | | time_stamp | datetime | +----------------+----------+ User_id是该表的主键。 每一行都包含ID为user_id的用户的注册时间信息。 表: Confirmations +----------------+----------+ | Column Name | Type | +----------------+----------+ | user_id | int | | time_stamp | datetime | | action | ENUM | +----------------+----------+ (user_id, time_stamp)是该表的主键。 user_id是一个引用到注册表的外键。 action是类型为('confirmed'， 'timeout')的ENUM 该表的每一行都表示ID为user_id的用户在time_stamp请求了一条确认消息，该确认消息要么被确认('confirmed')，要么被过期('timeout')。 用户的 确认率 是 'confirmed' 消息的数量除以请求的确认消息的总数。没有请求任何确认消息的用户的确认率为 0 。确认率四舍五入到 小数点后两位 。 编写一个SQL查询来查找每个用户的 确认率 。 以 任意顺序 返回结果表。 查询结果格式如下所示。 示例1: 输入： Signups 表: +---------+---------------------+ | user_id | time_stamp | +---------+---------------------+ | 3 | 2020-03-21 10:16:13 | | 7 | 2020-01-04 13:57:59 | | 2 | 2020-07-29 23:09:44 | | 6 | 2020-12-09 10:39:37 | +---------+---------------------+ Confirmations 表: +---------+---------------------+-----------+ | user_id | time_stamp | action | +---------+---------------------+-----------+ | 3 | 2021-01-06 03:30:46 | timeout | | 3 | 2021-07-14 14:00:00 | timeout | | 7 | 2021-06-12 11:57:29 | confirmed | | 7 | 2021-06-13 12:58:28 | confirmed | | 7 | 2021-06-14 13:59:27 | confirmed | | 2 | 2021-01-22 00:00:00 | confirmed | | 2 | 2021-02-28 23:59:59 | timeout | +---------+---------------------+-----------+ 输出: +---------+-------------------+ | user_id | confirmation_rate | +---------+-------------------+ | 6 | 0.00 | | 3 | 0.00 | | 7 | 1.00 | | 2 | 0.50 | +---------+-------------------+ 解释: 用户 6 没有请求任何确认消息。确认率为 0。 用户 3 进行了 2 次请求，都超时了。确认率为 0。 用户 7 提出了 3 个请求，所有请求都得到了确认。确认率为 1。 用户 2 做了 2 个请求，其中一个被确认，另一个超时。确认率为 1 / 2 = 0.5。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用 SQL 查询来计算每个用户的确认率。
- 首先，我们需要计算每个用户的确认消息数量和总请求消息数量。
- 然后，通过这些数量计算确认率，并四舍五入到小数点后两位。

算法步骤:
1. 计算每个用户的确认消息数量。
2. 计算每个用户的总请求消息数量。
3. 计算每个用户的确认率。
4. 四舍五入确认率到小数点后两位。
5. 返回结果表。

关键点:
- 使用子查询来计算每个用户的确认消息数量和总请求消息数量。
- 使用 CASE WHEN 语句来区分确认消息和超时消息。
- 使用 ROUND 函数来四舍五入确认率。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 Confirmations 表的行数。
空间复杂度: O(1)，因为只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(signups: List[List[int]], confirmations: List[List[str]]) -> List[List[float]]:
    """
    函数式接口 - 计算每个用户的确认率
    """
    # 创建 Signups 和 Confirmations 表
    signups_table = {row[0]: row[1] for row in signups}
    confirmations_table = {}
    
    # 统计每个用户的确认消息数量和总请求消息数量
    for user_id, _, action in confirmations:
        if user_id not in confirmations_table:
            confirmations_table[user_id] = {'confirmed': 0, 'total': 0}
        confirmations_table[user_id]['total'] += 1
        if action == 'confirmed':
            confirmations_table[user_id]['confirmed'] += 1
    
    # 计算每个用户的确认率
    result = []
    for user_id in signups_table:
        if user_id in confirmations_table:
            confirmed = confirmations_table[user_id]['confirmed']
            total = confirmations_table[user_id]['total']
            confirmation_rate = round(confirmed / total, 2) if total > 0 else 0.00
        else:
            confirmation_rate = 0.00
        result.append([user_id, confirmation_rate])
    
    return result


Solution = create_solution(solution_function_name)