# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3074
标题: Select Data
难度: easy
链接: https://leetcode.cn/problems/select-data/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2880. 数据选取 - DataFrame students +-------------+--------+ | Column Name | Type | +-------------+--------+ | student_id | int | | name | object | | age | int | +-------------+--------+ 编写一个解决方案，选择 student_id = 101 的学生的 name 和 age 并输出。 返回结果格式如下示例所示。 示例 1: 输入： +------------+---------+-----+ | student_id | name | age | +------------+---------+-----+ | 101 | Ulysses | 13 | | 53 | William | 10 | | 128 | Henry | 6 | | 3 | Henry | 11 | +------------+---------+-----+ 输出： +---------+-----+ | name | age | +---------+-----+ | Ulysses | 13 | +---------+-----+ 解释： 学生 Ulysses 的 student_id = 101，所以我们输出了他的 name 和 age。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Pandas 库的 DataFrame 进行数据筛选。

算法步骤:
1. 从输入的 DataFrame 中筛选出 student_id 为 101 的行。
2. 选择筛选后的行中的 name 和 age 列。
3. 返回包含 name 和 age 列的新 DataFrame。

关键点:
- 使用 Pandas 的 loc 方法进行高效的数据筛选。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 DataFrame 的行数。因为我们需要遍历整个 DataFrame 来找到符合条件的行。
空间复杂度: O(1)，因为我们只返回了筛选后的 DataFrame，没有使用额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd
from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(students: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 选择 student_id = 101 的学生的 name 和 age 并输出。
    """
    # 筛选出 student_id 为 101 的行
    filtered_students = students[students['student_id'] == 101]
    
    # 选择 name 和 age 列
    result = filtered_students[['name', 'age']]
    
    return result


Solution = create_solution(solution_function_name)