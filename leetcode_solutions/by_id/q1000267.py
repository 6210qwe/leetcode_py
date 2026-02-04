```python
# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000267
标题: O(1) 时间插入、删除和获取随机元素
难度: medium
链接: https://leetcode.cn/problems/FortPu/
题目类型: 设计、数组、哈希表、数学、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 030. O(1) 时间插入、删除和获取随机元素 - 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构： * insert(val)：当元素 val 不存在时返回 true ，并向集合中插入该项，否则返回 false 。 * remove(val)：当元素 val 存在时返回 true ，并从集合中移除该项，否则返回 false 。 * getRandom：随机返回现有集合中的一项。每个元素应该有 相同的概率 被返回。 示例 1： 输入: inputs = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"] [[], [1], [2], [2], [], [1], [2], []] 输出: [null, true, false, true, 2, true, false, 2] 解释: RandomizedSet randomSet = new RandomizedSet(); // 初始化一个空的集合 randomSet.insert(1); // 向集合中插入 1 ， 返回 true 表示 1 被成功地插入 randomSet.remove(2); // 返回 false，表示集合中不存在 2 randomSet.insert(2); // 向集合中插入 2 返回 true ，集合现在包含 [1,2] randomSet.getRandom(); // getRandom 应随机返回 1 或 2 randomSet.remove(1); // 从集合中移除 1 返回 true 。集合现在包含 [2] randomSet.insert(2); // 2 已在集合中，所以返回 false randomSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 提示： * -231 <= val <= 231 - 1 * 最多进行 2 * 105 次 insert ， remove 和 getRandom 方法调用 * 当调用 getRandom 方法时，集合中至少有一个元素 注意：本题与主站 380 题相同：https://leetcode.cn/problems/insert-delete-getrandom-o1/ [https://leetcode.cn/problems/insert-delete-getrandom-o1/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个列表来存储元素，并使用一个哈希表来记录每个元素在列表中的索引，从而实现 O(1) 时间复杂度的插入、删除和获取随机元素。

算法步骤:
1. 插入时，检查哈希表中是否存在该元素，如果存在则返回 False；否则将元素添加到列表末尾，并在哈希表中记录其索引。
2. 删除时，检查哈希表中是否存在该元素，如果不存在则返回 False；否则将该元素与列表末尾的元素交换位置，更新哈希表中末尾元素的索引，然后删除列表末尾的元素。
3. 获取随机元素时，直接从列表中随机选择一个元素。

关键点:
- 使用列表和哈希表结合的方式，确保插入、删除和获取随机元素的时间复杂度为 O(1)。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(1)
空间复杂度: O(n)，其中 n 是集合中元素的数量。
"""

# ============================================================================
# 代码实现
# ============================================================================

import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_val = self.values[-1]
        self.values[index] = last_val
        self.val_to_index[last_val] = index
        del self.val_to_index[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# 测试用例
if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(1))  # True
    print(obj.remove(2))  # False
    print(obj.insert(2))  # True
    print(obj.getRandom())  # 1 or 2
    print(obj.remove(1))  # True
    print(obj.insert(2))  # False
    print(obj.getRandom())  # 2
```

这个实现使用了列表和哈希表来确保插入、删除和获取随机元素的操作都在 O(1) 时间复杂度内完成。代码结构清晰，变量命名明确，并且包含了必要的注释。