# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 398
标题: Random Pick Index
难度: medium
链接: https://leetcode.cn/problems/random-pick-index/
题目类型: 水塘抽样、哈希表、数学、随机化
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
398. 随机数索引 - 给你一个可能含有 重复元素 的整数数组 nums ，请你随机输出给定的目标数字 target 的索引。你可以假设给定的数字一定存在于数组中。 实现 Solution 类： * Solution(int[] nums) 用数组 nums 初始化对象。 * int pick(int target) 从 nums 中选出一个满足 nums[i] == target 的随机索引 i 。如果存在多个有效的索引，则每个索引的返回概率应当相等。 示例： 输入 ["Solution", "pick", "pick", "pick"] [[[1, 2, 3, 3, 3]], [3], [1], [3]] 输出 [null, 4, 0, 2] 解释 Solution solution = new Solution([1, 2, 3, 3, 3]); solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。 solution.pick(1); // 返回 0 。因为只有 nums[0] 等于 1 。 solution.pick(3); // 随机返回索引 2, 3 或者 4 之一。每个索引的返回概率应该相等。 提示： * 1 <= nums.length <= 2 * 104 * -231 <= nums[i] <= 231 - 1 * target 是 nums 中的一个整数 * 最多调用 pick 函数 104 次
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 预处理每个值的所有下标列表，随机返回其中一个；由于每个下标都有同等概率被选中，满足题意。

算法步骤:
1. 在构造函数中遍历数组 `nums`，用哈希表 `pos` 将值映射到所有出现下标的列表。
2. 对于 pick(target)，从 `pos[target]` 中使用 `random.choice` 随机返回一个下标。

关键点:
- 预处理一次，后续每次查询只做 O(1) 的随机访问。
- 题目保证 target 一定在数组中，因此无需处理不存在的情况（如需更安全可加判断）。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: 构造函数 O(n)，n 为数组长度；每次 pick 为 O(1)。
空间复杂度: O(n)，存储所有下标。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


import random


class RandomPickIndex:
    """
    随机返回目标值在数组中的索引，若有多个索引则等概率返回。

    预处理 value -> indices 列表，pick 时在对应列表中随机选一个。
    """

    def __init__(self, nums: List[int]):
        from collections import defaultdict

        self.pos = defaultdict(list)
        for i, v in enumerate(nums):
            self.pos[v].append(i)

    def pick(self, target: int) -> int:
        arr = self.pos[target]
        return random.choice(arr)


def random_pick_index(nums: List[int]) -> RandomPickIndex:
    """
    函数式接口 - 返回 RandomPickIndex 实例。
    """
    return RandomPickIndex(nums)


# 自动生成Solution类（无需手动编写）
Solution = create_solution(random_pick_index)
