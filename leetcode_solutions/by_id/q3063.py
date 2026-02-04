# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3063
标题: Method Chaining
难度: easy
链接: https://leetcode.cn/problems/method-chaining/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2891. 方法链 - DataFrame animals +-------------+--------+ | Column Name | Type | +-------------+--------+ | name | object | | species | object | | age | int | | weight | int | +-------------+--------+ 编写一个解决方案来列出体重 严格超过 100 千克的动物的名称。 按体重 降序 返回动物。 返回结果格式如下示例所示。 示例 1: 输入： DataFrame animals: +----------+---------+-----+--------+ | name | species | age | weight | +----------+---------+-----+--------+ | Tatiana | Snake | 98 | 464 | | Khaled | Giraffe | 50 | 41 | | Alex | Leopard | 6 | 328 | | Jonathan | Monkey | 45 | 463 | | Stefan | Bear | 100 | 50 | | Tommy | Panda | 26 | 349 | +----------+---------+-----+--------+ 输出： +----------+ | name | +----------+ | Tatiana | | Jonathan | | Tommy | | Alex | +----------+ 解释： 所有体重超过 100 的动物都应包含在结果表中。 Tatiana 的体重为 464，Jonathan 的体重为 463，Tommy 的体重为 349，Alex 的体重为 328。 结果应按体重降序排序。 在 Pandas 中，方法链 允许我们在 DataFrame 上执行操作，而无需将每个操作拆分成单独的行或创建多个临时变量。 你能用 一行 代码的方法链完成这个任务吗？
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用Pandas的DataFrame方法链来筛选和排序数据。

算法步骤:
1. 筛选出体重严格超过100千克的动物。
2. 按体重降序排序。
3. 选择动物名称列。

关键点:
- 使用Pandas的`query`方法进行筛选。
- 使用`sort_values`方法进行排序。
- 使用`[[]]`选择特定列。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n log n)，其中n是DataFrame的行数。主要由排序操作决定。
空间复杂度: O(1)，方法链操作不使用额外的空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd
from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(animals: pd.DataFrame) -> pd.DataFrame:
    """
    函数式接口 - 使用Pandas方法链筛选并排序动物
    """
    # 使用方法链筛选并排序
    result = animals.query('weight > 100').sort_values(by='weight', ascending=False)[['name']]
    return result


Solution = create_solution(solution_function_name)