# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 380
标题: Insert Delete GetRandom O(1)
难度: medium
链接: https://leetcode.cn/problems/insert-delete-getrandom-o1/
题目类型: 设计、数组、哈希表、数学、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
380. O(1) 时间插入、删除和获取随机元素 - 实现RandomizedSet 类： * RandomizedSet() 初始化 RandomizedSet 对象 * bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。 * bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。 * int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。 你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。 示例： 输入 ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"] [[], [1], [2], [2], [], [1], [2], []] 输出 [null, true, false, true, 2, true, false, 2] 解释 RandomizedSet randomizedSet = new RandomizedSet(); randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。 randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。 randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。 randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。 randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。 randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。 randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。 提示： * -231 <= val <= 231 - 1 * 最多调用 insert、remove 和 getRandom 函数 2 * 105 次 * 在调用 getRandom 方法时，数据结构中 至少存在一个 元素。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [待实现] 根据题目类型实现相应算法

算法步骤:
1. [待实现] 分析题目要求
2. [待实现] 设计算法流程
3. [待实现] 实现核心逻辑

关键点:
- [待实现] 注意边界条件
- [待实现] 优化时间和空间复杂度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([待分析]) - 需要根据具体实现分析
空间复杂度: O([待分析]) - 需要根据具体实现分析
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
import random
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


class RandomizedSet:
    """
    支持 O(1) 平均时间插入、删除和随机获取元素的数据结构。

    通过数组保存元素，哈希表记录元素到数组下标的映射，
    删除时将待删元素与数组末尾元素交换，再弹出末尾即可。
    """

    def __init__(self):
        self.nums: List[int] = []
        self.pos: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last_val = self.nums[-1]
        # 将最后一个元素移到 idx 位置
        self.nums[idx] = last_val
        self.pos[last_val] = idx
        # 删除末尾
        self.nums.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


def insert_delete_getrandom_o1() -> RandomizedSet:
    """
    函数式接口 - 返回一个 RandomizedSet 实例，便于在测试中进行方法调用。
    """
    return RandomizedSet()


# 自动生成Solution类（无需手动编写）
Solution = create_solution(insert_delete_getrandom_o1)
