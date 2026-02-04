# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3076
标题: Get the Size of a DataFrame
难度: easy
链接: https://leetcode.cn/problems/get-the-size-of-a-dataframe/
题目类型: 其他
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2878. 获取 DataFrame 的大小 - DataFrame players: +-------------+--------+ | Column Name | Type | +-------------+--------+ | player_id | int | | name | object | | age | int | | position | object | | ... | ... | +-------------+--------+ 编写一个解决方案，计算并显示 players 的 行数和列数。 将结果返回为一个数组： [number of rows, number of columns] 返回结果格式如下示例所示。 示例 1： 输入： +-----------+----------+-----+-------------+--------------------+ | player_id | name | age | position | team | +-----------+----------+-----+-------------+--------------------+ | 846 | Mason | 21 | Forward | RealMadrid | | 749 | Riley | 30 | Winger | Barcelona | | 155 | Bob | 28 | Striker | ManchesterUnited | | 583 | Isabella | 32 | Goalkeeper | Liverpool | | 388 | Zachary | 24 | Midfielder | BayernMunich | | 883 | Ava | 23 | Defender | Chelsea | | 355 | Violet | 18 | Striker | Juventus | | 247 | Thomas | 27 | Striker | ParisSaint-Germain | | 761 | Jack | 33 | Midfielder | ManchesterCity | | 642 | Charlie | 36 | Center-back | Arsenal | +-----------+----------+-----+-------------+--------------------+ 输出： [10, 5] 解释： 这个 DataFrame 包含 10 行和 5 列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用 pandas 库提供的 shape 属性来获取 DataFrame 的行数和列数。

算法步骤:
1. 导入 pandas 库。
2. 使用 pandas 的 shape 属性获取 DataFrame 的行数和列数。
3. 返回包含行数和列数的列表。

关键点:
- pandas 库提供了高效的方法来处理 DataFrame。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - 获取 DataFrame 的 shape 属性是常数时间操作。
空间复杂度: O(1) - 只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

import pandas as pd
from typing import List

def get_dataframe_size(players: pd.DataFrame) -> List[int]:
    """
    函数式接口 - 获取 DataFrame 的行数和列数
    """
    # 获取 DataFrame 的行数和列数
    num_rows, num_cols = players.shape
    return [num_rows, num_cols]

Solution = create_solution(get_dataframe_size)