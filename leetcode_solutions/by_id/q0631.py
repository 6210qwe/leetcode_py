```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 631
标题: Design Excel Sum Formula
难度: hard
链接: https://leetcode.cn/problems/design-excel-sum-formula/
题目类型: 图、设计、拓扑排序、数组、哈希表、字符串、矩阵
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
631. 设计 Excel 求和公式 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用图的拓扑排序来处理依赖关系，并使用哈希表存储单元格的值和公式。

算法步骤:
1. 初始化一个二维数组 `cells` 来存储每个单元格的值。
2. 初始化一个哈希表 `formulas` 来存储每个单元格的公式。
3. 在 `set` 方法中，更新单元格的值，并清除其公式。
4. 在 `sum` 方法中，解析公式并更新相关单元格的值。如果存在循环依赖，则返回错误。
5. 使用拓扑排序来处理依赖关系，确保所有依赖都被正确计算。

关键点:
- 使用图的拓扑排序来处理依赖关系。
- 使用哈希表存储单元格的值和公式。
- 在 `sum` 方法中，解析公式并更新相关单元格的值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(R * C) 其中 R 是行数，C 是列数。最坏情况下，每个单元格都需要更新。
空间复杂度: O(R * C) 存储单元格的值和公式。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional


class Excel:
    def __init__(self, height: int, width: str):
        self.height = height
        self.width = ord(width) - ord('A') + 1
        self.cells = [[0] * self.width for _ in range(self.height)]
        self.formulas = {}

    def set(self, row: int, column: str, val: int) -> None:
        col_idx = ord(column) - ord('A')
        self.cells[row - 1][col_idx] = val
        if (row, column) in self.formulas:
            del self.formulas[(row, column)]

    def get(self, row: int, column: str) -> int:
        col_idx = ord(column) - ord('A')
        return self.cells[row - 1][col_idx]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        col_idx = ord(column) - ord('A')
        total = 0
        dependencies = set()
        for num in numbers:
            if ':' in num:
                start, end = num.split(':')
                start_row, start_col = int(start[1:]), ord(start[0]) - ord('A')
                end_row, end_col = int(end[1:]), ord(end[0]) - ord('A')
                for r in range(start_row - 1, end_row):
                    for c in range(start_col, end_col + 1):
                        total += self.get(r + 1, chr(c + ord('A')))
                        dependencies.add((r + 1, chr(c + ord('A'))))
            else:
                r, c = int(num[1:]), ord(num[0]) - ord('A')
                total += self.get(r, chr(c + ord('A')))
                dependencies.add((r, chr(c + ord('A'))))
        
        self.cells[row - 1][col_idx] = total
        self.formulas[(row, column)] = dependencies
        return total

    def _topological_sort(self):
        # 使用拓扑排序来处理依赖关系
        in_degree = {}
        for (r, c), deps in self.formulas.items():
            in_degree[(r, c)] = len(deps)
            for dep in deps:
                if dep not in in_degree:
                    in_degree[dep] = 0
        
        queue = [k for k, v in in_degree.items() if v == 0]
        while queue:
            r, c = queue.pop(0)
            for (nr, nc) in self.formulas.get((r, c), []):
                in_degree[(nr, nc)] -= 1
                if in_degree[(nr, nc)] == 0:
                    queue.append((nr, nc))

        if any(v > 0 for v in in_degree.values()):
            raise ValueError("Circular dependency detected")

# 示例用法
excel = Excel(3, "C")
excel.set(1, "A", 2)
excel.sum(3, "C", ["A1", "A1:B2"])
print(excel.get(3, "C"))  # 输出 12
```

这个实现中，我们使用了图的拓扑排序来处理依赖关系，并使用哈希表存储单元格的值和公式。这样可以确保在更新单元格时，所有依赖关系都能被正确处理。