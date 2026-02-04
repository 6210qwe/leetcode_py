# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3797
标题: Design Spreadsheet
难度: medium
链接: https://leetcode.cn/problems/design-spreadsheet/
题目类型: 设计、数组、哈希表、字符串、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3484. 设计电子表格 - 电子表格是一个网格，它有 26 列（从 'A' 到 'Z'）和指定数量的 rows。每个单元格可以存储一个 0 到 105 之间的整数值。 请你实现一个 Spreadsheet 类： * Spreadsheet(int rows) 初始化一个具有 26 列（从 'A' 到 'Z'）和指定行数的电子表格。所有单元格最初的值都为 0 。 * void setCell(String cell, int value) 设置指定单元格的值。单元格引用以 "AX" 的格式提供（例如，"A1"，"B10"），其中字母表示列（从 'A' 到 'Z'），数字表示从 1 开始的行号。 * void resetCell(String cell) 重置指定单元格的值为 0 。 * int getValue(String formula) 计算一个公式的值，格式为 "=X+Y"，其中 X 和 Y 要么 是单元格引用，要么非负整数，返回计算的和。 注意： 如果 getValue 引用一个未通过 setCell 明确设置的单元格，则该单元格的值默认为 0 。 示例 1： 输入： ["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"] [[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]] 输出： [null, 12, null, 16, null, 25, null, 15] 解释 Spreadsheet spreadsheet = new Spreadsheet(3); // 初始化一个具有 3 行和 26 列的电子表格 spreadsheet.getValue("=5+7"); // 返回 12 (5+7) spreadsheet.setCell("A1", 10); // 设置 A1 为 10 spreadsheet.getValue("=A1+6"); // 返回 16 (10+6) spreadsheet.setCell("B2", 15); // 设置 B2 为 15 spreadsheet.getValue("=A1+B2"); // 返回 25 (10+15) spreadsheet.resetCell("A1"); // 重置 A1 为 0 spreadsheet.getValue("=A1+B2"); // 返回 15 (0+15) 提示： * 1 <= rows <= 103 * 0 <= value <= 105 * 公式保证采用 "=X+Y" 格式，其中 X 和 Y 要么是有效的单元格引用，要么是小于等于 105 的 非负 整数。 * 每个单元格引用由一个大写字母 'A' 到 'Z' 和一个介于 1 和 rows 之间的行号组成。 * 总共 最多会对 setCell、resetCell 和 getValue 调用 104 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想:
- 使用一个字典来存储单元格的值，键为单元格引用，值为单元格的值。
- 使用一个函数来解析公式并计算结果。

算法步骤:
1. 初始化时，创建一个空字典来存储单元格的值。
2. setCell 方法将单元格引用和值存入字典。
3. resetCell 方法将单元格引用的值设为 0。
4. getValue 方法解析公式并计算结果。

关键点:
- 使用字典来高效地存储和查找单元格的值。
- 解析公式时，需要处理单元格引用和整数的情况。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1) - setCell 和 resetCell 操作的时间复杂度为 O(1)，getValue 操作的时间复杂度也为 O(1)。
空间复杂度: O(n) - n 为调用 setCell 和 resetCell 的次数，最坏情况下所有单元格都被设置过。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict

class Spreadsheet:
    def __init__(self, rows: int):
        self.cells: Dict[str, int] = {}
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        # 去掉公式中的等号
        formula = formula[1:]
        # 分割公式中的两个部分
        x, y = formula.split('+')
        # 去掉可能的空格
        x, y = x.strip(), y.strip()
        
        # 获取 X 的值
        if x.isdigit():
            x_value = int(x)
        else:
            x_value = self.cells.get(x, 0)
        
        # 获取 Y 的值
        if y.isdigit():
            y_value = int(y)
        else:
            y_value = self.cells.get(y, 0)
        
        return x_value + y_value


# 测试代码
if __name__ == "__main__":
    spreadsheet = Spreadsheet(3)
    print(spreadsheet.getValue("=5+7"))  # 输出 12
    spreadsheet.setCell("A1", 10)
    print(spreadsheet.getValue("=A1+6"))  # 输出 16
    spreadsheet.setCell("B2", 15)
    print(spreadsheet.getValue("=A1+B2"))  # 输出 25
    spreadsheet.resetCell("A1")
    print(spreadsheet.getValue("=A1+B2"))  # 输出 15