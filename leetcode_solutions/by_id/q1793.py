# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1793
标题: Minimum Moves to Make Array Complementary
难度: medium
链接: https://leetcode.cn/problems/minimum-moves-to-make-array-complementary/
题目类型: 数组、哈希表、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1674. 使数组互补的最少操作次数 - 给你一个长度为 偶数 n 的整数数组 nums 和一个整数 limit 。每一次操作，你可以将 nums 中的任何整数替换为 1 到 limit 之间的另一个整数。 如果对于所有下标 i（下标从 0 开始），nums[i] + nums[n - 1 - i] 都等于同一个数，则数组 nums 是 互补的 。例如，数组 [1,2,3,4] 是互补的，因为对于所有下标 i ，nums[i] + nums[n - 1 - i] = 5 。 返回使数组 互补 的 最少 操作次数。 示例 1： 输入：nums = [1,2,4,3], limit = 4 输出：1 解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）： nums[0] + nums[3] = 1 + 3 = 4. nums[1] + nums[2] = 2 + 2 = 4. nums[2] + nums[1] = 2 + 2 = 4. nums[3] + nums[0] = 3 + 1 = 4. 对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。 示例 2： 输入：nums = [1,2,2,1], limit = 2 输出：2 解释：经过 2 次操作，你可以将数组 nums 变成 [2,2,2,2] 。你不能将任何数字变更为 3 ，因为 3 > limit 。 示例 3： 输入：nums = [1,2,1,2], limit = 2 输出：0 解释：nums 已经是互补的。 提示： * n == nums.length * 2 <= n <= 105 * 1 <= nums[i] <= limit <= 105 * n 是偶数。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 差分数组，对每个数对计算不同目标值需要的操作次数

算法步骤:
1. 对每个数对(a, b)，计算不同目标值需要的操作次数
2. 使用差分数组记录操作次数的变化
3. 找到最小操作次数

关键点:
- 差分数组优化
- 时间复杂度O(n*limit)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n*limit) - n为数组长度的一半
空间复杂度: O(limit) - 差分数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_moves(nums: List[int], limit: int) -> int:
    """
    函数式接口 - 使数组互补的最少操作次数
    
    实现思路:
    差分数组：对每个数对计算不同目标值需要的操作次数。
    
    Args:
        nums: 整数数组
        limit: 限制值
        
    Returns:
        最少操作次数
        
    Example:
        >>> min_moves([1,2,4,3], 4)
        1
    """
    n = len(nums)
    diff = [0] * (2 * limit + 2)
    
    for i in range(n // 2):
        a, b = nums[i], nums[n - 1 - i]
        
        # 不操作的情况
        min_sum = min(a, b) + 1
        max_sum = max(a, b) + limit
        
        # 0次操作
        diff[a + b] -= 1
        diff[a + b + 1] += 1
        
        # 1次操作
        diff[min_sum] += 1
        diff[max_sum + 1] -= 1
        
        # 2次操作
        diff[2] += 2
        diff[min_sum] -= 2
        diff[max_sum + 1] += 2
        diff[2 * limit + 1] -= 2
    
    result = float('inf')
    current = 0
    
    for target in range(2, 2 * limit + 1):
        current += diff[target]
        result = min(result, current)
    
    return result


Solution = create_solution(min_moves)
