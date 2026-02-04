# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2312
标题: Most Frequent Number Following Key In an Array
难度: easy
链接: https://leetcode.cn/problems/most-frequent-number-following-key-in-an-array/
题目类型: 数组、哈希表、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2190. 数组中紧跟 key 之后出现最频繁的数字 - 给你一个下标从 0 开始的整数数组 nums ，同时给你一个整数 key ，它在 nums 出现过。 统计 在 nums 数组中紧跟着 key 后面出现的不同整数 target 的出现次数。换言之，target 的出现次数为满足以下条件的 i 的数目： * 0 <= i <= n - 2 * nums[i] == key 且 * nums[i + 1] == target 。 请你返回出现 最多 次数的 target 。测试数据保证出现次数最多的 target 是唯一的。 示例 1： 输入：nums = [1,100,200,1,100], key = 1 输出：100 解释：对于 target = 100 ，在下标 1 和 4 处出现过 2 次，且都紧跟着 key 。 没有其他整数在 key 后面紧跟着出现，所以我们返回 100 。 示例 2： 输入：nums = [2,2,2,2,3], key = 2 输出：2 解释：对于 target = 2 ，在下标 1 ，2 和 3 处出现过 3 次，且都紧跟着 key 。 对于 target = 3 ，在下标 4 出出现过 1 次，且紧跟着 key 。 target = 2 是紧跟着 key 之后出现次数最多的数字，所以我们返回 2 。 提示： * 2 <= nums.length <= 1000 * 1 <= nums[i] <= 1000 * 测试数据保证答案是唯一的。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表来记录每个 target 的出现次数，并找到出现次数最多的 target。

算法步骤:
1. 初始化一个字典 `count` 来记录每个 target 的出现次数。
2. 遍历数组 `nums`，对于每个元素 `nums[i]`，如果 `nums[i] == key`，则更新 `count[nums[i + 1]]`。
3. 找到 `count` 中出现次数最多的 target 并返回。

关键点:
- 使用哈希表来记录每个 target 的出现次数，时间复杂度为 O(n)。
- 一次遍历即可完成统计，空间复杂度为 O(1)（因为 target 的取值范围有限）。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(1)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def most_frequent_number_following_key(nums: List[int], key: int) -> int:
    """
    函数式接口 - 返回数组中紧跟 key 之后出现最频繁的数字
    """
    count = {}
    for i in range(len(nums) - 1):
        if nums[i] == key:
            if nums[i + 1] in count:
                count[nums[i + 1]] += 1
            else:
                count[nums[i + 1]] = 1
    
    # 找到出现次数最多的 target
    max_count = 0
    result = None
    for target, cnt in count.items():
        if cnt > max_count:
            max_count = cnt
            result = target
    
    return result


Solution = create_solution(most_frequent_number_following_key)