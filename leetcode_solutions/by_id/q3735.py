# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3735
标题: Design a 3D Binary Matrix with Efficient Layer Tracking
难度: medium
链接: https://leetcode.cn/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/
题目类型: 设计、数组、哈希表、矩阵、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3391. 设计一个高效的层跟踪三维二进制矩阵 - 备战技术面试？力扣提供海量技术面试资源，帮助你高效提升编程技能,轻松拿下世界 IT 名企 Dream Offer。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用字典来存储每一层的非零元素，并使用有序集合来维护每一层的非零元素索引。

算法步骤:
1. 初始化一个字典 `layers` 来存储每一层的非零元素。
2. 初始化一个有序集合 `non_zero_indices` 来存储每一层的非零元素索引。
3. 提供 `set_value` 方法来设置指定位置的值，并更新 `layers` 和 `non_zero_indices`。
4. 提供 `get_value` 方法来获取指定位置的值。
5. 提供 `get_non_zero_layers` 方法来获取所有包含非零元素的层。

关键点:
- 使用字典和有序集合来高效地管理和查询非零元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 对于每个操作，有序集合的插入和删除操作的时间复杂度为 O(log n)。
空间复杂度: O(n) - 字典和有序集合的空间复杂度为 O(n)，其中 n 是非零元素的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional, Set
from sortedcontainers import SortedSet

class Solution:
    def __init__(self):
        self.layers = {}  # 存储每一层的非零元素
        self.non_zero_indices = SortedSet()  # 存储每一层的非零元素索引

    def set_value(self, x: int, y: int, z: int, value: int) -> None:
        """
        设置指定位置 (x, y, z) 的值为 value。
        """
        if value == 0:
            if (x, y) in self.layers and z in self.layers[(x, y)]:
                del self.layers[(x, y)][z]
                self.non_zero_indices.discard((x, y, z))
        else:
            if (x, y) not in self.layers:
                self.layers[(x, y)] = {}
            self.layers[(x, y)][z] = value
            self.non_zero_indices.add((x, y, z))

    def get_value(self, x: int, y: int, z: int) -> int:
        """
        获取指定位置 (x, y, z) 的值。
        """
        if (x, y) in self.layers and z in self.layers[(x, y)]:
            return self.layers[(x, y)][z]
        return 0

    def get_non_zero_layers(self) -> Set[tuple]:
        """
        获取所有包含非零元素的层。
        """
        return {index[:2] for index in self.non_zero_indices}

# 示例用法
if __name__ == "__main__":
    matrix = Solution()
    matrix.set_value(0, 0, 0, 1)
    matrix.set_value(0, 0, 1, 2)
    print(matrix.get_value(0, 0, 0))  # 输出: 1
    print(matrix.get_non_zero_layers())  # 输出: {(0, 0)}