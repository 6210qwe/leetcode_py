# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000234
标题: 全排列
难度: medium
链接: https://leetcode.cn/problems/VvJkup/
题目类型: 数组、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 083. 全排列 - 给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。 示例 1： 输入：nums = [1,2,3] 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 示例 2： 输入：nums = [0,1] 输出：[[0,1],[1,0]] 示例 3： 输入：nums = [1] 输出：[[1]] 提示： * 1 <= nums.length <= 6 * -10 <= nums[i] <= 10 * nums 中的所有整数 互不相同 注意：本题与主站 46 题相同：https://leetcode.cn/problems/permutations/ [https://leetcode.cn/problems/permutations/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 回溯生成所有排列

算法步骤:
1. 使用回溯函数 dfs(path, used)：
   - 若 path 长度等于 nums 长度，将 path 的拷贝加入答案
   - 否则，遍历 nums 中的每个元素：
       * 若该元素未被使用，则标记为使用并将其加入 path
       * 递归调用 dfs
       * 回溯时弹出元素并取消使用标记
2. 初始时 path 为空，used 全为 False

关键点:
- 使用 used 数组跟踪当前路径中使用过的元素
- nums 中元素互不相同，不需要特殊去重逻辑
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * n!) - n! 个排列，每个排列长度为 n
空间复杂度: O(n) - 递归栈和 used 标记
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def permute(nums: List[int]) -> List[List[int]]:
    """
    函数式接口 - 全排列
    """
    res: List[List[int]] = []
    n = len(nums)
    used = [False] * n
    path: List[int] = []

    def dfs() -> None:
        if len(path) == n:
            res.append(path[:])
            return
        for i in range(n):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return res


Solution = create_solution(permute)
