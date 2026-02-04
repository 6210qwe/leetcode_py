# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2555
标题: Design SQL
难度: medium
链接: https://leetcode.cn/problems/design-sql/
题目类型: 设计、数组、哈希表、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2408. 设计 SQL - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典来存储表和列的信息，并使用列表来存储行数据。

算法步骤:
1. 初始化一个字典来存储表和列的信息，以及一个字典来存储行数据。
2. 在创建表时，将表名和列信息存入表字典中。
3. 在插入数据时，将数据存入行数据字典中。
4. 在查询数据时，根据条件过滤行数据并返回结果。

关键点:
- 使用字典来快速查找表和列的信息。
- 使用列表来存储行数据，并在查询时进行过滤。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 其中 n 是行数据的数量，最坏情况下需要遍历所有行数据。
空间复杂度: O(m + n) - 其中 m 是表和列信息的总大小，n 是行数据的总大小。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution

class SQL:

    def __init__(self):
        self.tables = {}  # 存储表和列的信息
        self.data = {}  # 存储行数据

    def create_table(self, table_name: str, columns: List[str]) -> None:
        """
        创建表
        :param table_name: 表名
        :param columns: 列名列表
        """
        self.tables[table_name] = columns
        self.data[table_name] = []

    def insert_row(self, table_name: str, row: List[str]) -> None:
        """
        插入一行数据
        :param table_name: 表名
        :param row: 数据行
        """
        if table_name in self.tables and len(row) == len(self.tables[table_name]):
            self.data[table_name].append(row)
        else:
            raise ValueError("Invalid table name or row length")

    def select_cell(self, table_name: str, column_name: str, row_id: int) -> str:
        """
        查询指定单元格的数据
        :param table_name: 表名
        :param column_name: 列名
        :param row_id: 行ID
        :return: 单元格数据
        """
        if table_name not in self.tables or column_name not in self.tables[table_name]:
            raise ValueError("Invalid table name or column name")
        if row_id < 0 or row_id >= len(self.data[table_name]):
            raise ValueError("Invalid row id")
        column_index = self.tables[table_name].index(column_name)
        return self.data[table_name][row_id][column_index]

    def select_where(self, table_name: str, column_name: str, value: str) -> List[List[str]]:
        """
        根据条件查询数据
        :param table_name: 表名
        :param column_name: 列名
        :param value: 查询值
        :return: 符合条件的数据行
        """
        if table_name not in self.tables or column_name not in self.tables[table_name]:
            raise ValueError("Invalid table name or column name")
        column_index = self.tables[table_name].index(column_name)
        result = []
        for row in self.data[table_name]:
            if row[column_index] == value:
                result.append(row)
        return result


Solution = create_solution(SQL)