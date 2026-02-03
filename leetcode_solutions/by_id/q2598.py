# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 2598
标题: Shortest Distance to Target String in a Circular Array
难度: easy
链接: https://leetcode.cn/problems/shortest-distance-to-target-string-in-a-circular-array/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
2515. 到目标字符串的最短距离 - 给你一个下标从 0 开始的 环形 字符串数组 words 和一个字符串 target 。环形数组 意味着数组首尾相连。 * 形式上， words[i] 的下一个元素是 words[(i + 1) % n] ，而 words[i] 的前一个元素是 words[(i - 1 + n) % n] ，其中 n 是 words 的长度。 从 startIndex 开始，你一次可以用 1 步移动到下一个或者前一个单词。 返回到达目标字符串 target 所需的最短距离。如果 words 中不存在字符串 target ，返回 -1 。 示例 1： 输入：words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1 输出：1 解释：从下标 1 开始，可以经由以下步骤到达 "hello" ： - 向右移动 3 个单位，到达下标 4 。 - 向左移动 2 个单位，到达下标 4 。 - 向右移动 4 个单位，到达下标 0 。 - 向左移动 1 个单位，到达下标 0 。 到达 "hello" 的最短距离是 1 。 示例 2： 输入：words = ["a","b","leetcode"], target = "leetcode", startIndex = 0 输出：1 解释：从下标 0 开始，可以经由以下步骤到达 "leetcode" ： - 向右移动 2 个单位，到达下标 3 。 - 向左移动 1 个单位，到达下标 3 。 到达 "leetcode" 的最短距离是 1 。 示例 3： 输入：words = ["i","eat","leetcode"], target = "ate", startIndex = 0 输出：-1 解释：因为 words 中不存在字符串 "ate" ，所以返回 -1 。 提示： * 1 <= words.length <= 100 * 1 <= words[i].length <= 100 * words[i] 和 target 仅由小写英文字母组成 * 0 <= startIndex < words.length
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: [TODO]

算法步骤:
1. [TODO]
2. [TODO]

关键点:
- [TODO]
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O([TODO])
空间复杂度: O([TODO])
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def solution_function_name(params):
    """
    函数式接口 - [TODO] 实现
    """
    # TODO: 实现最优解法
    pass


Solution = create_solution(solution_function_name)
