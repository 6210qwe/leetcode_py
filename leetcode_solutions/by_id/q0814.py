# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 814
标题: Smallest Rotation with Highest Score
难度: hard
链接: https://leetcode.cn/problems/smallest-rotation-with-highest-score/
题目类型: 数组、前缀和
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
798. 得分最高的最小轮调 - 给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为 [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。 * 例如，数组为 nums = [2,4,1,3,0]，我们按 k = 2 进行轮调后，它将变成 [1,3,0,2,4]。这将记为 3 分，因为 1 > 0 [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。 在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。 示例 1： 输入：nums = [2,3,1,4,0] 输出：3 解释： 下面列出了每个 k 的得分： k = 0, nums = [2,3,1,4,0], score 2 k = 1, nums = [3,1,4,0,2], score 3 k = 2, nums = [1,4,0,2,3], score 3 k = 3, nums = [4,0,2,3,1], score 4 k = 4, nums = [0,2,3,1,4], score 3 所以我们应当选择 k = 3，得分最高。 示例 2： 输入：nums = [1,3,0,2,4] 输出：0 解释： nums 无论怎么变化总是有 3 分。 所以我们将选择最小的 k，即 0。 提示： * 1 <= nums.length <= 105 * 0 <= nums[i] < nums.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用差分数组来计算每个轮调后的得分，并找到得分最高的轮调下标。

算法步骤:
1. 初始化差分数组 diff 和当前得分 current_score。
2. 计算初始得分 current_score。
3. 遍历每个可能的轮调 k，更新差分数组并计算新的得分。
4. 记录得分最高的轮调下标。

关键点:
- 使用差分数组来高效地更新得分。
- 通过遍历每个可能的轮调 k 来找到最优解。
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


def solution_function_name(nums: List[int]) -> int:
    """
    函数式接口 - 找到得分最高的最小轮调下标
    """
    n = len(nums)
    diff = [0] * (n + 1)
    current_score = 0
    
    # 计算初始得分
    for i in range(n):
        if nums[i] <= i:
            current_score += 1
            diff[0] += 1
            diff[i - nums[i] + 1] -= 1
        else:
            diff[i + 1] += 1
            diff[n - (nums[i] - i)] -= 1
    
    max_score = current_score
    best_k = 0
    
    # 遍历每个可能的轮调 k
    for k in range(1, n):
        current_score += diff[k]
        if current_score > max_score:
            max_score = current_score
            best_k = k
    
    return best_k


Solution = create_solution(solution_function_name)