# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1505
标题: Create Target Array in the Given Order
难度: easy
链接: https://leetcode.cn/problems/create-target-array-in-the-given-order/
题目类型: 数组、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1389. 按既定顺序创建目标数组 - 给你两个整数数组 nums 和 index。你需要按照以下规则创建目标数组： * 目标数组 target 最初为空。 * 按从左到右的顺序依次读取 nums[i] 和 index[i]，在 target 数组中的下标 index[i] 处插入值 nums[i] 。 * 重复上一步，直到在 nums 和 index 中都没有要读取的元素。 请你返回目标数组。 题目保证数字插入位置总是存在。 示例 1： 输入：nums = [0,1,2,3,4], index = [0,1,2,2,1] 输出：[0,4,1,3,2] 解释： nums index target 0 0 [0] 1 1 [0,1] 2 2 [0,1,2] 3 2 [0,1,3,2] 4 1 [0,4,1,3,2] 示例 2： 输入：nums = [1,2,3,4,0], index = [0,1,2,3,0] 输出：[0,1,2,3,4] 解释： nums index target 1 0 [1] 2 1 [1,2] 3 2 [1,2,3] 4 3 [1,2,3,4] 0 0 [0,1,2,3,4] 示例 3： 输入：nums = [1], index = [0] 输出：[1] 提示： * 1 <= nums.length, index.length <= 100 * nums.length == index.length * 0 <= nums[i] <= 100 * 0 <= index[i] <= i
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用列表的 insert 方法按给定顺序插入元素。

算法步骤:
1. 初始化一个空的目标数组 `target`。
2. 遍历 `nums` 和 `index` 数组，对于每个 `i`，在 `target` 的 `index[i]` 位置插入 `nums[i]`。
3. 返回最终的 `target` 数组。

关键点:
- 利用 Python 列表的 `insert` 方法来实现插入操作。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n^2)，其中 n 是 nums 的长度。每次插入操作的时间复杂度为 O(n)。
空间复杂度: O(n)，目标数组 `target` 的空间消耗。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def create_target_array(nums: List[int], index: List[int]) -> List[int]:
    """
    函数式接口 - 按既定顺序创建目标数组
    """
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target


Solution = create_solution(create_target_array)