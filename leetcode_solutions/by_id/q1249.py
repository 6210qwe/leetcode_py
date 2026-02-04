```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1249
标题: Snapshot Array
难度: medium
链接: https://leetcode.cn/problems/snapshot-array/
题目类型: 设计、数组、哈希表、二分查找
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1146. 快照数组 - 实现支持下列接口的「快照数组」- SnapshotArray： * SnapshotArray(int length) - 初始化一个与指定长度相等的 类数组 的数据结构。初始时，每个元素都等于 0。 * void set(index, val) - 会将指定索引 index 处的元素设置为 val。 * int snap() - 获取该数组的快照，并返回快照的编号 snap_id（快照号是调用 snap() 的总次数减去 1）。 * int get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。 示例： 输入：["SnapshotArray","set","snap","set","get"] [[3],[0,5],[],[0,6],[0,0]] 输出：[null,null,0,null,5] 解释： SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组 snapshotArr.set(0,5); // 令 array[0] = 5 snapshotArr.snap(); // 获取快照，返回 snap_id = 0 snapshotArr.set(0,6); snapshotArr.get(0,0); // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5 提示： * 1 <= length <= 50000 * 题目最多进行50000 次set，snap，和 get的调用 。 * 0 <= index < length * 0 <= snap_id < 我们调用 snap() 的总次数 * 0 <= val <= 10^9
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表存储每个索引在不同快照中的值，并使用二分查找来高效地获取特定快照的值。

算法步骤:
1. 初始化时，创建一个字典，用于存储每个索引在不同快照中的值。
2. 在 set 方法中，更新当前快照的值。
3. 在 snap 方法中，增加快照编号并返回当前快照编号。
4. 在 get 方法中，使用二分查找找到指定快照编号的值。

关键点:
- 使用字典存储每个索引在不同快照中的值。
- 使用二分查找来高效地获取特定快照的值。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 
- set: O(1)
- snap: O(1)
- get: O(log n)，其中 n 是快照的数量

空间复杂度: O(n * m)，其中 n 是数组的长度，m 是快照的数量
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = {i: [] for i in range(length)}

    def set(self, index: int, val: int) -> None:
        if not self.data[index] or self.data[index][-1][0] != self.snap_id:
            self.data[index].append((self.snap_id, val))
        else:
            self.data[index][-1] = (self.snap_id, val)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshots = self.data[index]
        left, right = 0, len(snapshots) - 1
        while left <= right:
            mid = (left + right) // 2
            if snapshots[mid][0] == snap_id:
                return snapshots[mid][1]
            elif snapshots[mid][0] < snap_id:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0:
            return snapshots[right][1]
        return 0


# 测试用例
if __name__ == "__main__":
    snapshot_arr = SnapshotArray(3)
    snapshot_arr.set(0, 5)
    print(snapshot_arr.snap())  # 输出 0
    snapshot_arr.set(0, 6)
    print(snapshot_arr.get(0, 0))  # 输出 5
```

这个实现中，`SnapshotArray` 类使用了哈希表来存储每个索引在不同快照中的值，并使用二分查找来高效地获取特定快照的值。这样可以确保 `set` 和 `snap` 操作的时间复杂度为 O(1)，而 `get` 操作的时间复杂度为 O(log n)。