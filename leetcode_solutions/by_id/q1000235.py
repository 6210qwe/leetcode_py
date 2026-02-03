# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1000235
标题: 全排列 II
难度: medium
链接: https://leetcode.cn/problems/7p8L0Z/
题目类型: 数组、回溯
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
LCR 084. 全排列 II - 给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。 示例 1： 输入：nums = [1,1,2] 输出： [[1,1,2], [1,2,1], [2,1,1]] 示例 2： 输入：nums = [1,2,3] 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]] 提示： * 1 <= nums.length <= 8 * -10 <= nums[i] <= 10 注意：本题与主站 47 题相同： https://leetcode.cn/problems/permutations-ii/ [https://leetcode.cn/problems/permutations-ii/]
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 排序 + 回溯 + 同层剪枝避免重复

算法步骤:
1. 对 nums 排序，将相同元素相邻放置
2. 使用回溯函数 dfs(path, used)：
   - 若 path 长度等于 nums 长度，将 path 的拷贝加入答案
   - 否则遍历每个下标 i：
       * 若 used[i] 为 True，跳过
       * 若 i > 0 且 nums[i] == nums[i-1] 且 used[i-1] 为 False，跳过（同层重复）
       * 选择 nums[i]，标记 used[i]，加入 path，递归 dfs
       * 回溯后弹出元素并取消 used[i]

关键点:
- “同层”去重条件：当前数字与前一个相同且前一个在本层未被使用（即 used[i-1] == False）
- 排序是去重的前提
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n * n!) - 最坏情况接近全排列复杂度
空间复杂度: O(n) - 递归栈与 used 数组
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    函数式接口 - 全排列 II
    """
    nums.sort()
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
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(nums[i])
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return res


Solution = create_solution(permute_unique)
