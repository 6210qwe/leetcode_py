# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 39
标题: Combination Sum
难度: medium
链接: https://leetcode.cn/problems/combination-sum/
题目类型: 数组、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
39. 组合总和 - 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。 candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 对于给定的输入，保证和为 target 的不同组合数少于 150 个。 示例 1： 输入：candidates = [2,3,6,7], target = 7 输出：[[2,2,3],[7]] 解释： 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。 7 也是一个候选， 7 = 7 。 仅有这两种组合。 示例 2： 输入: candidates = [2,3,5], target = 8 输出: [[2,2,2,2],[2,3,3],[3,5]] 示例 3： 输入: candidates = [2], target = 1 输出: [] 提示： * 1 <= candidates.length <= 30 * 2 <= candidates[i] <= 40 * candidates 的所有元素 互不相同 * 1 <= target <= 40
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯算法，每个数字可以无限次使用，按顺序尝试所有组合

算法步骤:
1. 对数组排序，便于剪枝
2. 使用回溯，从当前位置开始尝试所有可能的组合
3. 如果和等于target，加入结果；如果和大于target，剪枝

关键点:
- 回溯+剪枝，避免重复组合
- 时间复杂度O(2^target)，空间复杂度O(target)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^target) - 组合数
空间复杂度: O(target) - 递归栈深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    函数式接口 - 组合总和
    
    实现思路:
    回溯算法，每个数字可以无限次使用，按顺序尝试所有组合。
    
    Args:
        candidates: 无重复元素的整数数组
        target: 目标整数
        
    Returns:
        所有不同组合的列表
        
    Example:
        >>> combination_sum([2,3,6,7], 7)
        [[2, 2, 3], [7]]
    """
    result = []
    candidates.sort()
    
    def backtrack(start: int, path: List[int], remaining: int):
        """回溯函数"""
        if remaining == 0:
            result.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(combination_sum)
