# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2388
标题: Replace Elements in an Array
难度: medium
链接: https://leetcode.cn/problems/replace-elements-in-an-array/
题目类型: 数组、哈希表、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2295. 替换数组中的元素 - 给你一个下标从 0 开始的数组 nums ，它包含 n 个 互不相同 的正整数。请你对这个数组执行 m 个操作，在第 i 个操作中，你需要将数字 operations[i][0] 替换成 operations[i][1] 。 题目保证在第 i 个操作中： * operations[i][0] 在 nums 中存在。 * operations[i][1] 在 nums 中不存在。 请你返回执行完所有操作后的数组。 示例 1： 输入：nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]] 输出：[3,2,7,1] 解释：我们对 nums 执行以下操作： - 将数字 1 替换为 3 。nums 变为 [3,2,4,6] 。 - 将数字 4 替换为 7 。nums 变为 [3,2,7,6] 。 - 将数字 6 替换为 1 。nums 变为 [3,2,7,1] 。 返回最终数组 [3,2,7,1] 。 示例 2： 输入：nums = [1,2], operations = [[1,3],[2,1],[3,2]] 输出：[2,1] 解释：我们对 nums 执行以下操作： - 将数字 1 替换为 3 。nums 变为 [3,2] 。 - 将数字 2 替换为 1 。nums 变为 [3,1] 。 - 将数字 3 替换为 2 。nums 变为 [2,1] 。 返回最终数组 [2,1] 。 提示： * n == nums.length * m == operations.length * 1 <= n, m <= 105 * nums 中所有数字 互不相同 。 * operations[i].length == 2 * 1 <= nums[i], operations[i][0], operations[i][1] <= 106 * 在执行第 i 个操作时，operations[i][0] 在 nums 中存在。 * 在执行第 i 个操作时，operations[i][1] 在 nums 中不存在。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用哈希表记录每个元素的新值，并在最后更新数组。

算法步骤:
1. 创建一个哈希表 `value_map` 来记录每个元素的新值。
2. 遍历 `operations`，对于每个操作，更新 `value_map`。
3. 遍历 `nums`，使用 `value_map` 更新每个元素的值。
4. 返回更新后的 `nums`。

关键点:
- 使用哈希表可以在 O(1) 时间内查找和更新元素的新值。
- 最后一次性更新 `nums`，避免多次修改数组。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n + m)，其中 n 是 `nums` 的长度，m 是 `operations` 的长度。
空间复杂度: O(n)，需要额外的空间来存储 `value_map`。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def replace_elements(nums: List[int], operations: List[List[int]]) -> List[int]:
    """
    函数式接口 - 替换数组中的元素
    """
    # 创建一个哈希表来记录每个元素的新值
    value_map = {num: num for num in nums}
    
    # 遍历 operations，更新 value_map
    for old_val, new_val in operations:
        value_map[old_val] = new_val
    
    # 更新 nums
    for i in range(len(nums)):
        nums[i] = value_map[nums[i]]
    
    return nums


Solution = create_solution(replace_elements)