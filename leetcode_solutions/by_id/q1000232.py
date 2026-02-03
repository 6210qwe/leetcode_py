# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000232
标题: 组合总和 II
难度: medium
链接: https://leetcode.cn/problems/4sjJUc/
题目类型: 数组、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 082. 组合总和 II - 给定一个可能有重复数字的整数数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 candidates 中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。 示例 1： 输入：candidates = [10,1,2,7,6,1,5], target = 8 输出： [ [1,1,6], [1,2,5], [1,7], [2,6] ] 示例 2： 输入：candidates = [2,5,2,1,2], target = 5 输出： [ [1,2,2], [5] ] 提示： * 1 <= candidates.length <= 100 * 1 <= candidates[i] <= 50 * 1 <= target <= 30 注意：本题与主站 40 题相同： https://leetcode.cn/problems/combination-sum-ii/ [https://leetcode.cn/problems/combination-sum-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯 + 排序 + 同层去重

算法步骤:
1. 先对 candidates 排序，方便后续剪枝和去重
2. 使用回溯函数 dfs(start, path, remain)：
   - 若 remain == 0，将当前 path 加入答案
   - 若 remain < 0，剪枝返回
   - 从下标 start 开始遍历 i：
       * 若 i > start 且 candidates[i] == candidates[i-1]，跳过以避免同层重复
       * 若 candidates[i] > remain，可以直接 break（后面更大）
       * 选择 candidates[i] 加入 path，递归 dfs(i+1, path + [candidates[i]], remain - candidates[i])
3. 初始调用 dfs(0, [], target)

关键点:
- 数组排序后，同一层遇到相同的数字需要跳过，防止重复组合
- 每个数字只能使用一次，所以递归下一层的起点是 i+1
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(2^n) 级别（取决于解的多少与剪枝效果），n 为 candidates 长度
空间复杂度: O(n) - 递归栈与路径存储
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    函数式接口 - 组合总和 II
    """
    candidates.sort()
    res: List[List[int]] = []
    n = len(candidates)

    def dfs(start: int, path: List[int], remain: int) -> None:
        if remain == 0:
            res.append(path[:])
            return
        if remain < 0:
            return
        for i in range(start, n):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            val = candidates[i]
            if val > remain:
                break
            path.append(val)
            dfs(i + 1, path, remain - val)
            path.pop()

    dfs(0, [], target)
    return res


Solution = create_solution(combination_sum2)
