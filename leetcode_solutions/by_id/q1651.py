# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1651
标题: Shuffle String
难度: easy
链接: https://leetcode.cn/problems/shuffle-string/
题目类型: 数组、字符串
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1528. 重新排列字符串 - 给你一个字符串 s 和一个 长度相同 的整数数组 indices 。 请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。 返回重新排列后的字符串。 示例 1： [https://assets.leetcode.cn/aliyun-lc-upload/uploads/2020/07/26/q1.jpg] 输入：s = "codeleet", indices = [4,5,6,7,0,2,1,3] 输出："leetcode" 解释：如图所示，"codeleet" 重新排列后变为 "leetcode" 。 示例 2： 输入：s = "abc", indices = [0,1,2] 输出："abc" 解释：重新排列后，每个字符都还留在原来的位置上。 提示： * s.length == indices.length == n * 1 <= n <= 100 * s 仅包含小写英文字母 * 0 <= indices[i] < n * indices 的所有的值都是 唯一 的
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用一个新字符串来存储重新排列后的结果。

算法步骤:
1. 初始化一个长度为 len(s) 的空字符串 result。
2. 遍历 indices 数组，将 s 中的字符按照 indices 的指示位置放入 result 中。
3. 返回 result。

关键点:
- 使用一个新字符串来存储结果，避免多次修改原字符串。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。我们需要遍历整个 indices 数组一次。
空间复杂度: O(n)，我们使用了一个新的字符串来存储结果。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def restore_string(s: str, indices: List[int]) -> str:
    """
    函数式接口 - 重新排列字符串
    """
    # 初始化一个长度为 len(s) 的空字符串 result
    result = [''] * len(s)
    
    # 遍历 indices 数组，将 s 中的字符按照 indices 的指示位置放入 result 中
    for i in range(len(s)):
        result[indices[i]] = s[i]
    
    # 返回 result
    return ''.join(result)


Solution = create_solution(restore_string)