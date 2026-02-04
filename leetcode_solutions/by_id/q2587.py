# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2587
标题: Design Memory Allocator
难度: medium
链接: https://leetcode.cn/problems/design-memory-allocator/
题目类型: 设计、数组、哈希表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2502. 设计内存分配器 - 给你一个整数 n ，表示下标从 0 开始的内存数组的大小。所有内存单元开始都是空闲的。 请你设计一个具备以下功能的内存分配器： 1. 分配 一块大小为 size 的连续空闲内存单元并赋 id mID 。 2. 释放 给定 id mID 对应的所有内存单元。 注意： * 多个块可以被分配到同一个 mID 。 * 你必须释放 mID 对应的所有内存单元，即便这些内存单元被分配在不同的块中。 实现 Allocator 类： * Allocator(int n) 使用一个大小为 n 的内存数组初始化 Allocator 对象。 * int allocate(int size, int mID) 找出大小为 size 个连续空闲内存单元且位于 最左侧 的块，分配并赋 id mID 。返回块的第一个下标。如果不存在这样的块，返回 -1 。 * int freeMemory(int mID) 释放 id mID 对应的所有内存单元。返回释放的内存单元数目。 示例： 输入 ["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"] [[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]] 输出 [null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0] 解释 Allocator loc = new Allocator(10); // 初始化一个大小为 10 的内存数组，所有内存单元都是空闲的。 loc.allocate(1, 1); // 最左侧的块的第一个下标是 0 。内存数组变为 [1, , , , , , , , , ]。返回 0 。 loc.allocate(1, 2); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,2, , , , , , , , ]。返回 1 。 loc.allocate(1, 3); // 最左侧的块的第一个下标是 2 。内存数组变为 [1,2,3, , , , , , , ]。返回 2 。 loc.freeMemory(2); // 释放 mID 为 2 的所有内存单元。内存数组变为 [1, ,3, , , , , , , ] 。返回 1 ，因为只有 1 个 mID 为 2 的内存单元。 loc.allocate(3, 4); // 最左侧的块的第一个下标是 3 。内存数组变为 [1, ,3,4,4,4, , , , ]。返回 3 。 loc.allocate(1, 1); // 最左侧的块的第一个下标是 1 。内存数组变为 [1,1,3,4,4,4, , , , ]。返回 1 。 loc.allocate(1, 1); // 最左侧的块的第一个下标是 6 。内存数组变为 [1,1,3,4,4,4,1, , , ]。返回 6 。 loc.freeMemory(1); // 释放 mID 为 1 的所有内存单元。内存数组变为 [ , ,3,4,4,4, , , , ] 。返回 3 ，因为有 3 个 mID 为 1 的内存单元。 loc.allocate(10, 2); // 无法找出长度为 10 个连续空闲内存单元的空闲块，所有返回 -1 。 loc.freeMemory(7); // 释放 mID 为 7 的所有内存单元。内存数组保持原状，因为不存在 mID 为 7 的内存单元。返回 0 。 提示： * 1 <= n, size, mID <= 1000 * 最多调用 allocate 和 free 方法 1000 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来表示内存数组，并使用一个字典来记录每个 mID 对应的内存单元位置。

算法步骤:
1. 初始化时，创建一个大小为 n 的内存数组，并创建一个字典来记录每个 mID 对应的内存单元位置。
2. 在 allocate 方法中，遍历内存数组，找到第一个满足条件的连续空闲内存单元块，将其分配给 mID，并更新内存数组和字典。
3. 在 freeMemory 方法中，根据字典中的记录，释放 mID 对应的所有内存单元，并更新内存数组和字典。

关键点:
- 使用字典来记录每个 mID 对应的内存单元位置，便于快速释放内存。
- 在 allocate 方法中，通过遍历内存数组找到第一个满足条件的连续空闲内存单元块。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 在最坏情况下，allocate 方法需要遍历整个内存数组。
空间复杂度: O(n) - 需要一个大小为 n 的内存数组和一个字典来记录每个 mID 对应的内存单元位置。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional


class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n  # 内存数组
        self.mID_map = {}  # 记录每个 mID 对应的内存单元位置

    def allocate(self, size: int, mID: int) -> int:
        start = 0
        while start < len(self.memory):
            if self.memory[start] == 0:
                end = start + size
                if end > len(self.memory):
                    break
                if all(self.memory[i] == 0 for i in range(start, end)):
                    for i in range(start, end):
                        self.memory[i] = mID
                    if mID not in self.mID_map:
                        self.mID_map[mID] = []
                    self.mID_map[mID].extend(range(start, end))
                    return start
                else:
                    start = end
            else:
                start += 1
        return -1

    def freeMemory(self, mID: int) -> int:
        if mID not in self.mID_map:
            return 0
        for index in self.mID_map[mID]:
            self.memory[index] = 0
        freed_count = len(self.mID_map[mID])
        del self.mID_map[mID]
        return freed_count


# 示例测试
if __name__ == "__main__":
    allocator = Allocator(10)
    print(allocator.allocate(1, 1))  # 0
    print(allocator.allocate(1, 2))  # 1
    print(allocator.allocate(1, 3))  # 2
    print(allocator.freeMemory(2))   # 1
    print(allocator.allocate(3, 4))  # 3
    print(allocator.allocate(1, 1))  # 1
    print(allocator.allocate(1, 1))  # 6
    print(allocator.freeMemory(1))   # 3
    print(allocator.allocate(10, 2)) # -1
    print(allocator.freeMemory(7))   # 0