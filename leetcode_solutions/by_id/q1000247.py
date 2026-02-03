# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000247
标题: 连续数组
难度: medium
链接: https://leetcode.cn/problems/A1NYOS/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 011. 连续数组 - 给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。 示例 1： 输入: nums = [0,1] 输出: 2 解释: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。 示例 2： 输入: nums = [0,1,0] 输出: 2 解释: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。 提示： * 1 <= nums.length <= 105 * nums[i] 不是 0 就是 1 注意：本题与主站 525 题相同： https://leetcode.cn/problems/contiguous-array/ [https://leetcode.cn/problems/contiguous-array/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 将 0 看作 -1，前缀和相等表示 0 和 1 数量相等

算法步骤:
1. 将数组中的 0 替换为 -1，1 保持为 1（可以在计算前缀时逻辑处理）
2. 定义前缀和 prefix，初始为 0
3. 使用哈希表 first_index 记录某个前缀和第一次出现的下标：
   - 初始化 first_index[0] = -1，表示和为 0 在下标 -1 处出现
4. 遍历数组 nums，索引 i：
   - 若 nums[i] == 1，则 prefix += 1；若 nums[i] == 0，则 prefix -= 1
   - 若 prefix 在 first_index 中出现过，说明从 first_index[prefix]+1 到 i 的子数组和为 0（0 和 1 数量相等），更新最大长度
   - 否则记录 first_index[prefix] = i
5. 返回最大长度

关键点:
- 将二进制数组转换成和为 0 的问题
- 只记录前缀和第一次出现的位置以获得最长长度
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n)
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def find_max_length(nums: List[int]) -> int:
    """
    函数式接口 - 连续数组
    """
    prefix = 0
    first_index = {0: -1}
    max_len = 0

    for i, num in enumerate(nums):
        prefix += 1 if num == 1 else -1
        if prefix in first_index:
            max_len = max(max_len, i - first_index[prefix])
        else:
            first_index[prefix] = i

    return max_len


Solution = create_solution(find_max_length)
