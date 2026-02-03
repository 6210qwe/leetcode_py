# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1798
标题: Max Number of K-Sum Pairs
难度: medium
链接: https://leetcode.cn/problems/max-number-of-k-sum-pairs/
题目类型: 数组、哈希表、双指针、排序
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1679. K 和数对的最大数目 - 给你一个整数数组 nums 和一个整数 k 。 每一步操作中，你需要从数组中选出和为 k 的两个整数，并将它们移出数组。 返回你可以对数组执行的最大操作数。 示例 1： 输入：nums = [1,2,3,4], k = 5 输出：2 解释：开始时 nums = [1,2,3,4]： - 移出 1 和 4 ，之后 nums = [2,3] - 移出 2 和 3 ，之后 nums = [] 不再有和为 5 的数对，因此最多执行 2 次操作。 示例 2： 输入：nums = [3,1,3,4,3], k = 6 输出：1 解释：开始时 nums = [3,1,3,4,3]： - 移出前两个 3 ，之后nums = [1,4,3] 不再有和为 6 的数对，因此最多执行 1 次操作。 提示： * 1 <= nums.length <= 105 * 1 <= nums[i] <= 109 * 1 <= k <= 109
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 哈希表统计频率，贪心匹配

算法步骤:
1. 统计每个数字的出现频率
2. 遍历数组，对于每个数字num，查找k-num
3. 如果找到且频率>0，匹配一对，减少频率

关键点:
- 哈希表统计
- 贪心匹配
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n) - 遍历数组一次
空间复杂度: O(n) - 哈希表空间
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from collections import Counter
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def max_operations(nums: List[int], k: int) -> int:
    """
    函数式接口 - K 和数对的最大数目
    
    实现思路:
    哈希表统计频率，贪心匹配。
    
    Args:
        nums: 整数数组
        k: 目标和
        
    Returns:
        最大操作数
        
    Example:
        >>> max_operations([1,2,3,4], 5)
        2
    """
    counter = Counter(nums)
    count = 0
    
    for num in list(counter.keys()):
        complement = k - num
        
        if complement in counter:
            if num == complement:
                # 相同数字，需要至少2个
                pairs = counter[num] // 2
                count += pairs
                counter[num] -= pairs * 2
            else:
                # 不同数字，取较小频率
                pairs = min(counter[num], counter[complement])
                count += pairs
                counter[num] -= pairs
                counter[complement] -= pairs
    
    return count


Solution = create_solution(max_operations)
