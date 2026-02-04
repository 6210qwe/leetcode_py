# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 381
标题: Insert Delete GetRandom O(1) - Duplicates allowed
难度: hard
链接: https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/
题目类型: 设计、数组、哈希表、数学、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
381. O(1) 时间插入、删除和获取随机元素 - 允许重复 - RandomizedCollection 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。 实现 RandomizedCollection 类: * RandomizedCollection()初始化空的 RandomizedCollection 对象。 * bool insert(int val) 将一个 val 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 true ，否则返回 false 。 * bool remove(int val) 如果存在，从集合中移除一个 val 项。如果该项存在，则返回 true ，否则返回 false 。注意，如果 val 在集合中出现多次，我们只删除其中一个。 * int getRandom() 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 线性相关 。 您必须实现类的函数，使每个函数的 平均 时间复杂度为 O(1) 。 注意：生成测试用例时，只有在 RandomizedCollection 中 至少有一项 时，才会调用 getRandom 。 示例 1: 输入 ["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"] [[], [1], [1], [2], [], [1], []] 输出 [null, true, false, true, 2, true, 1] 解释 RandomizedCollection collection = new RandomizedCollection();// 初始化一个空的集合。 collection.insert(1); // 返回 true，因为集合不包含 1。 // 将 1 插入到集合中。 collection.insert(1); // 返回 false，因为集合包含 1。 // 将另一个 1 插入到集合中。集合现在包含 [1,1]。 collection.insert(2); // 返回 true，因为集合不包含 2。 // 将 2 插入到集合中。集合现在包含 [1,1,2]。 collection.getRandom(); // getRandom 应当: // 有 2/3 的概率返回 1, // 1/3 的概率返回 2。 collection.remove(1); // 返回 true，因为集合包含 1。 // 从集合中移除 1。集合现在包含 [1,2]。 collection.getRandom(); // getRandom 应该返回 1 或 2，两者的可能性相同。 提示: * -231 <= val <= 231 - 1 * insert, remove 和 getRandom 最多 总共 被调用 2 * 105 次 * 当调用 getRandom 时，数据结构中 至少有一个 元素
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 数组 +「值到下标集合」的哈希表，删除时与末尾元素交换，允许同一个值对应多个下标。

算法步骤:
1. 使用数组 `nums` 存储所有插入的元素，支持 O(1) 下标访问。
2. 使用哈希表 `indices`，将每个值映射到一个下标集合 `set[int]`，记录该值在 `nums` 中出现的所有位置。
3. insert: 将当前数组长度加入 `indices[val]`，并把 val 追加到 `nums`；只有在此前未出现过该值时返回 True。
4. remove: 从 `indices[val]` 中弹出任意一个下标 idx，取出 `nums` 末尾元素 last_val，若 idx 不是末尾位置，则将末尾元素移到 idx 并在 `indices[last_val]` 中更新旧下标为 idx，最后弹出数组末尾。
5. getRandom: 从 `nums` 中随机选取一个下标返回对应元素，重复值自然按出现次数线性加权。

关键点:
- 允许重复时，需要为每个值维护一个「下标集合」而不是单个下标。
- 删除时注意同步维护被移动到 idx 位置元素在哈希表中的下标集合。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: `insert`/`remove`/`getRandom` 平均均为 O(1)。 
空间复杂度: O(n)，n 为当前集合中元素个数，需要存储数组和哈希表。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import random
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class RandomizedCollection:
    """
    支持重复元素的 O(1) 平均时间插入、删除和随机获取数据结构。

    使用数组保存元素，哈希表记录值到所有下标的集合，
    删除时同样通过与末尾交换实现 O(1) 删除。
    """

    def __init__(self):
        self.nums: List[int] = []
        self.indices: dict[int, set[int]] = {}

    def insert(self, val: int) -> bool:
        existed = val in self.indices and self.indices[val]
        if not existed:
            self.indices.setdefault(val, set())
        self.indices[val].add(len(self.nums))
        self.nums.append(val)
        return not existed

    def remove(self, val: int) -> bool:
        if val not in self.indices or not self.indices[val]:
            return False
        # 取出该值的任意一个下标
        idx = self.indices[val].pop()
        last_val = self.nums[-1]
        if idx != len(self.nums) - 1:
            # 将最后一个元素移到 idx 位置
            self.nums[idx] = last_val
            # 更新 last_val 在 indices 中的下标集合
            self.indices[last_val].remove(len(self.nums) - 1)
            self.indices[last_val].add(idx)
        # 删除末尾元素
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


def insert_delete_getrandom_o1_duplicates_allowed() -> RandomizedCollection:
    """
    函数式接口 - 返回一个 RandomizedCollection 实例。
    """
    return RandomizedCollection()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(insert_delete_getrandom_o1_duplicates_allowed)
