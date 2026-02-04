# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3071
标题: Drop Duplicate Rows
难度: easy
链接: https://leetcode.cn/problems/drop-duplicate-rows/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2882. 删去重复的行 - DataFrame customers +-------------+--------+ | Column Name | Type | +-------------+--------+ | customer_id | int | | name | object | | email | object | +-------------+--------+ 在 DataFrame 中基于 email 列存在一些重复行。 编写一个解决方案，删除这些重复行，仅保留第一次出现的行。 返回结果格式如下例所示。 示例 1: 输入： +-------------+---------+---------------------+ | customer_id | name | email | +-------------+---------+---------------------+ | 1 | Ella | emily@example.com | | 2 | David | michael@example.com | | 3 | Zachary | sarah@example.com | | 4 | Alice | john@example.com | | 5 | Finn | john@example.com | | 6 | Violet | alice@example.com | +-------------+---------+---------------------+ 输出： +-------------+---------+---------------------+ | customer_id | name | email | +-------------+---------+---------------------+ | 1 | Ella | emily@example.com | | 2 | David | michael@example.com | | 3 | Zachary | sarah@example.com | | 4 | Alice | john@example.com | | 6 | Violet | alice@example.com | +-------------+---------+---------------------+ 解释： Alice (customer_id = 4) 和 Finn (customer_id = 5) 都使用 john@example.com，因此只保留该邮箱地址的第一次出现。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 pandas 的 drop_duplicates 方法来删除重复的行，基于 email 列，并保留第一次出现的行。

算法步骤:
1. 导入 pandas 库。
2. 使用 drop_duplicates 方法删除重复行，指定 email 列为依据，并保留第一次出现的行。
3. 返回处理后的 DataFrame。

关键点:
- 使用 drop_duplicates 方法可以高效地删除重复行。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是 DataFrame 的行数。drop_duplicates 方法的时间复杂度是线性的。
空间复杂度: O(1)，除了输入和输出外，不使用额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd

def drop_duplicate_rows(customers: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 删除 DataFrame 中基于 email 列的重复行，仅保留第一次出现的行。
    """
    # 使用 drop_duplicates 方法删除重复行，基于 email 列，并保留第一次出现的行
    return customers.drop_duplicates(subset='email', keep='first')

Solution = create_solution(drop_duplicate_rows)