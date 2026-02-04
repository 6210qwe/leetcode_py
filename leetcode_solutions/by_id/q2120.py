# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2120
标题: First and Last Call On the Same Day
难度: hard
链接: https://leetcode.cn/problems/first-and-last-call-on-the-same-day/
题目类型: 数据库
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1972. 同一天的第一个电话和最后一个电话 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用窗口函数来找到每天的第一个和最后一个电话记录。

算法步骤:
1. 使用窗口函数 `ROW_NUMBER()` 分别为每个用户的每个日期的电话记录分配一个行号，按时间升序和降序排列。
2. 通过连接两个子查询，分别找到每个用户每天的第一个和最后一个电话记录。
3. 选择所需的列并返回结果。

关键点:
- 使用窗口函数 `ROW_NUMBER()` 来标识每个用户每天的第一个和最后一个电话记录。
- 通过连接两个子查询来获取所需的结果。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中 n 是电话记录的数量。排序操作的时间复杂度为 O(n log n)。
空间复杂度: O(n)，需要存储中间结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

def solution_function_name(calls: List[List[str]]) -> List[List[str]]:
    """
    函数式接口 - 实现
    """
    # 将输入转换为 DataFrame
    import pandas as pd
    calls_df = pd.DataFrame(calls, columns=['user_id', 'call_time'])

    # 转换 call_time 列为 datetime 类型
    calls_df['call_time'] = pd.to_datetime(calls_df['call_time'])

    # 提取日期
    calls_df['call_date'] = calls_df['call_time'].dt.date

    # 按 user_id 和 call_date 排序
    calls_df = calls_df.sort_values(by=['user_id', 'call_date', 'call_time'])

    # 使用窗口函数 ROW_NUMBER() 为每个用户的每个日期的电话记录分配行号
    calls_df['row_num_asc'] = calls_df.groupby(['user_id', 'call_date']).cumcount() + 1
    calls_df['row_num_desc'] = calls_df.groupby(['user_id', 'call_date'])['call_time'].rank(method='dense', ascending=False)

    # 找到每个用户每天的第一个和最后一个电话记录
    first_calls = calls_df[calls_df['row_num_asc'] == 1]
    last_calls = calls_df[calls_df['row_num_desc'] == 1]

    # 合并第一个和最后一个电话记录
    result = pd.merge(first_calls, last_calls, on=['user_id', 'call_date'], suffixes=('_first', '_last'))

    # 选择所需的列
    result = result[['user_id', 'call_date', 'call_time_first', 'call_time_last']]

    # 将结果转换为列表
    result_list = result.values.tolist()

    return result_list

Solution = create_solution(solution_function_name)