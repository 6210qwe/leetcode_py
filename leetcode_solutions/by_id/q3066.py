# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3066
标题: Create a New Column
难度: easy
链接: https://leetcode.cn/problems/create-a-new-column/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2881. 创建新列 - DataFrame employees +-------------+--------+ | Column Name | Type. | +-------------+--------+ | name | object | | salary | int. | +-------------+--------+ 一家公司计划为员工提供奖金。 编写一个解决方案，创建一个名为 bonus 的新列，其中包含 salary 值的 两倍。 返回结果格式如下示例所示。 示例 1: 输入： DataFrame employees +---------+--------+ | name | salary | +---------+--------+ | Piper | 4548 | | Grace | 28150 | | Georgia | 1103 | | Willow | 6593 | | Finn | 74576 | | Thomas | 24433 | +---------+--------+ 输出： +---------+--------+--------+ | name | salary | bonus | +---------+--------+--------+ | Piper | 4548 | 9096 | | Grace | 28150 | 56300 | | Georgia | 1103 | 2206 | | Willow | 593 | 13186 | | Finn | 74576 | 149152 | | Thomas | 24433 | 48866 | +---------+--------+--------+ 解释： 通过将 salary 列中的值加倍创建了一个新的 bonus 列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 Pandas 库来处理 DataFrame，并在原 DataFrame 上添加新列。

算法步骤:
1. 导入 Pandas 库。
2. 读取输入的 DataFrame。
3. 创建一个新的列 'bonus'，其值为 'salary' 列的两倍。
4. 返回修改后的 DataFrame。

关键点:
- 使用 Pandas 库进行高效的数据处理。
- 直接在原 DataFrame 上添加新列，避免额外的空间开销。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 DataFrame 的行数。遍历一次 DataFrame 即可完成操作。
空间复杂度: O(1)，除了返回的结果外，不使用额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd
from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(employees: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 在给定的 DataFrame 中添加一个新列 'bonus'，其值为 'salary' 列的两倍。
    """
    # 创建一个新的列 'bonus'，其值为 'salary' 列的两倍
    employees['bonus'] = employees['salary'] * 2
    return employees


Solution = create_solution(solution_function_name)