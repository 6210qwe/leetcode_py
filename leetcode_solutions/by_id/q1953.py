# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1953
标题: Finding MK Average
难度: hard
链接: https://leetcode.cn/problems/finding-mk-average/
题目类型: 设计、队列、数据流、有序集合、堆（优先队列）
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1825. 求出 MK 平均值 - 给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。 MK 平均值 按照如下步骤计算： 1. 如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。 2. 从这个容器中删除最小的 k 个数和最大的 k 个数。 3. 计算剩余元素的平均值，并 向下取整到最近的整数 。 请你实现 MKAverage 类： * MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。 * void addElement(int num) 往数据流中插入一个新的元素 num 。 * int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。 示例 1： 输入： ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"] [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []] 输出： [null, null, null, -1, null, 3, null, null, null, 5] 解释： MKAverage obj = new MKAverage(3, 1); obj.addElement(3); // 当前元素为 [3] obj.addElement(1); // 当前元素为 [3,1] obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素 obj.addElement(10); // 当前元素为 [3,1,10] obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10] // 删除最小以及最大的 1 个元素后，容器为 [3] // [3] 的平均值等于 3/1 = 3 ，故返回 3 obj.addElement(5); // 当前元素为 [3,1,10,5] obj.addElement(5); // 当前元素为 [3,1,10,5,5] obj.addElement(5); // 当前元素为 [3,1,10,5,5,5] obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5] // 删除最小以及最大的 1 个元素后，容器为 [5] // [5] 的平均值等于 5/1 = 5 ，故返回 5 提示： * 3 <= m <= 105 * 1 <= k*2 < m * 1 <= num <= 105 * addElement 与 calculateMKAverage 总操作次数不超过 105 次。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用有序列表 (SortedList) 来维护数据流中的最后 m 个元素，并在需要时快速删除最小和最大的 k 个元素。

算法步骤:
1. 初始化时，创建一个有序列表来存储数据流中的元素。
2. 在 addElement 方法中，将新元素添加到有序列表中，并在超过 m 个元素时移除最旧的元素。
3. 在 calculateMKAverage 方法中，如果数据流中的元素少于 m 个，返回 -1；否则，使用有序列表快速删除最小和最大的 k 个元素，然后计算剩余元素的平均值。

关键点:
- 使用 SortedList 来高效地维护有序数据。
- 在计算平均值时，直接从有序列表中获取中间部分的元素。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(log m) - 添加和删除元素的时间复杂度。
空间复杂度: O(m) - 存储最后 m 个元素的空间复杂度。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.data_stream = []
        self.sorted_data = SortedList()

    def addElement(self, num: int) -> None:
        self.data_stream.append(num)
        self.sorted_data.add(num)
        if len(self.data_stream) > self.m:
            removed_num = self.data_stream.pop(0)
            self.sorted_data.remove(removed_num)

    def calculateMKAverage(self) -> int:
        if len(self.data_stream) < self.m:
            return -1
        middle_part = self.sorted_data[self.k:-self.k]
        return sum(middle_part) // len(middle_part)


# 示例测试
if __name__ == "__main__":
    obj = MKAverage(3, 1)
    obj.addElement(3)
    obj.addElement(1)
    print(obj.calculateMKAverage())  # -1
    obj.addElement(10)
    print(obj.calculateMKAverage())  # 3
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    print(obj.calculateMKAverage())  # 5