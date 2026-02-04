# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2434
标题: Design a Number Container System
难度: medium
链接: https://leetcode.cn/problems/design-a-number-container-system/
题目类型: 设计、哈希表、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2349. 设计数字容器系统 - 设计一个数字容器系统，可以实现以下功能： * 在系统中给定下标处 插入 或者 替换 一个数字。 * 返回 系统中给定数字的最小下标。 请你实现一个 NumberContainers 类： * NumberContainers() 初始化数字容器系统。 * void change(int index, int number) 在下标 index 处填入 number 。如果该下标 index 处已经有数字了，那么用 number 替换该数字。 * int find(int number) 返回给定数字 number 在系统中的最小下标。如果系统中没有 number ，那么返回 -1 。 示例： 输入： ["NumberContainers", "find", "change", "change", "change", "change", "find", "change", "find"] [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]] 输出： [null, -1, null, null, null, null, 1, null, 2] 解释： NumberContainers nc = new NumberContainers(); nc.find(10); // 没有数字 10 ，所以返回 -1 。 nc.change(2, 10); // 容器中下标为 2 处填入数字 10 。 nc.change(1, 10); // 容器中下标为 1 处填入数字 10 。 nc.change(3, 10); // 容器中下标为 3 处填入数字 10 。 nc.change(5, 10); // 容器中下标为 5 处填入数字 10 。 nc.find(10); // 数字 10 所在的下标为 1 ，2 ，3 和 5 。因为最小下标为 1 ，所以返回 1 。 nc.change(1, 20); // 容器中下标为 1 处填入数字 20 。注意，下标 1 处之前为 10 ，现在被替换为 20 。 nc.find(10); // 数字 10 所在下标为 2 ，3 和 5 。最小下标为 2 ，所以返回 2 。 提示： * 1 <= index, number <= 109 * 调用 change 和 find 的 总次数 不超过 105 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用两个字典来维护索引和数字的关系。一个字典用于存储每个索引对应的数字，另一个字典用于存储每个数字对应的索引集合，并使用有序集合来维护这些索引的顺序。

算法步骤:
1. 初始化两个字典：`index_to_number` 用于存储索引到数字的映射，`number_to_indices` 用于存储数字到索引集合的映射。
2. 在 `change` 方法中，更新 `index_to_number` 字典，并相应地更新 `number_to_indices` 字典。
3. 在 `find` 方法中，从 `number_to_indices` 字典中获取最小的索引。

关键点:
- 使用有序集合来维护每个数字的索引集合，以确保能够高效地获取最小索引。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log n) - 由于使用了有序集合，插入和查找操作的时间复杂度为 O(log n)。
空间复杂度: O(n) - 需要额外的空间来存储索引和数字的映射关系。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import Dict, Set
from sortedcontainers import SortedSet

class NumberContainers:

    def __init__(self):
        self.index_to_number: Dict[int, int] = {}
        self.number_to_indices: Dict[int, SortedSet] = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            self.number_to_indices[old_number].discard(index)
            if not self.number_to_indices[old_number]:
                del self.number_to_indices[old_number]

        self.index_to_number[index] = number
        if number not in self.number_to_indices:
            self.number_to_indices[number] = SortedSet()
        self.number_to_indices[number].add(index)

    def find(self, number: int) -> int:
        if number in self.number_to_indices and self.number_to_indices[number]:
            return self.number_to_indices[number][0]
        return -1


Solution = create_solution(NumberContainers)