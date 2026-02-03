# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 40
标题: Combination Sum II
难度: medium
链接: https://leetcode.cn/problems/combination-sum-ii/
题目类型: 数组、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
40. 组合总和 II - 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 candidates 中的每个数字在每个组合中只能使用 一次 。 注意：解集不能包含重复的组合。 示例 1: 输入: candidates = [10,1,2,7,6,1,5], target = 8, 输出: [ [1,1,6], [1,2,5], [1,7], [2,6] ] 示例 2: 输入: candidates = [2,5,2,1,2], target = 5, 输出: [ [1,2,2], [5] ] 提示: * 1 <= candidates.length <= 100 * 1 <= candidates[i] <= 50 * 1 <= target <= 30
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯算法，每个数字只能使用一次，需要去重

算法步骤:
1. 对数组排序
2. 使用回溯，跳过重复数字避免重复组合
3. 每个位置只能使用一次，从下一个位置开始

关键点:
- 回溯+去重，跳过相同数字
- 时间复杂度O(2^n)，空间复杂度O(target)
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n) - n为数组长度
空间复杂度: O(target) - 递归栈深度
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List
from leetcode_solutions.utils.solution import create_solution


def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    """
    函数式接口 - 组合总和II
    
    实现思路:
    回溯算法，每个数字只能使用一次，需要去重。
    
    Args:
        candidates: 候选人编号的集合（可能包含重复）
        target: 目标数
        
    Returns:
        所有可以使数字和为target的组合
        
    Example:
        >>> combination_sum_ii([10,1,2,7,6,1,5], 8)
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
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
            # 跳过重复数字
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, remaining - candidates[i])
            path.pop()
    
    backtrack(0, [], target)
    return result


# 自动生成Solution类（无需手动编写）
Solution = create_solution(combination_sum_ii)
