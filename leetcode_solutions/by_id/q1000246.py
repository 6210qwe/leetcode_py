# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000246
标题: 和为 K 的子数组
难度: medium
链接: https://leetcode.cn/problems/QTMn0o/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 010. 和为 K 的子数组 - 给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。 示例 1： 输入:nums = [1,1,1], k = 2 输出: 2 解释: 此题 [1,1] 与 [1,1] 为两种不同的情况 示例 2： 输入:nums = [1,2,3], k = 3 输出: 2 提示: * 1 <= nums.length <= 2 * 104 * -1000 <= nums[i] <= 1000 * -107 <= k <= 107 注意：本题与主站 560 题相同： https://leetcode.cn/problems/subarray-sum-equals-k/ [https://leetcode.cn/problems/subarray-sum-equals-k/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 前缀和 + 哈希表统计

算法步骤:
1. 定义前缀和 pre_sum[i] 为 nums[0..i-1] 的和（实现时可用一个变量累计）
2. 维护一个哈希表 counter，key 为某个前缀和的值，value 为该前缀和出现的次数
   - 初始化 counter[0] = 1，表示和为 0 的前缀和一开始出现一次
3. 遍历数组 nums：
   - 更新前缀和 sum += num
   - 我们希望找到以当前下标结尾、和为 k 的子数组个数，即前面有多少个前缀和等于 sum - k
   - 将 counter[sum - k] 加到答案中
   - 再将当前前缀和 sum 计入 counter
4. 遍历结束，返回答案

关键点:
- 使用前缀和差值 sum[i] - sum[j] == k 表示子数组 j..i-1 的和为 k
- 哈希表记录所有历史前缀和出现次数，实现 O(1) 查询
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)
空间复杂度: O(n) - 存储前缀和计数
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution
from collections import defaultdict


def subarray_sum(nums: List[int], k: int) -> int:
    """
    函数式接口 - 和为 K 的子数组
    """
    counter = defaultdict(int)
    counter[0] = 1
    prefix = 0
    ans = 0
    for num in nums:
        prefix += num
        ans += counter[prefix - k]
        counter[prefix] += 1
    return ans


Solution = create_solution(subarray_sum)
