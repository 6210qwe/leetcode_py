# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 3426
标题: Minimum Number of Chairs in a Waiting Room
难度: easy
链接: https://leetcode.cn/problems/minimum-number-of-chairs-in-a-waiting-room/
题目类型: 字符串、模拟
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
3168. 候诊室中的最少椅子数 - 给你一个字符串 s，模拟每秒钟的事件 i： * 如果 s[i] == 'E'，表示有一位顾客进入候诊室并占用一把椅子。 * 如果 s[i] == 'L'，表示有一位顾客离开候诊室，从而释放一把椅子。 返回保证每位进入候诊室的顾客都能有椅子坐的 最少 椅子数，假设候诊室最初是 空的 。 示例 1： 输入：s = "EEEEEEE" 输出：7 解释： 每秒后都有一个顾客进入候诊室，没有人离开。因此，至少需要 7 把椅子。 示例 2： 输入：s = "ELELEEL" 输出：2 解释： 假设候诊室里有 2 把椅子。下表显示了每秒钟等候室的状态。 秒 事件 候诊室的人数 可用的椅子数 0 Enter 1 1 1 Leave 0 2 2 Enter 1 1 3 Leave 0 2 4 Enter 1 1 5 Enter 2 0 6 Leave 1 1 示例 3： 输入：s = "ELEELEELLL" 输出：3 解释： 假设候诊室里有 3 把椅子。下表显示了每秒钟等候室的状态。 秒 事件 候诊室的人数 可用的椅子数 0 Enter 1 2 1 Leave 0 3 2 Enter 1 2 3 Enter 2 1 4 Leave 1 2 5 Enter 2 1 6 Enter 3 0 7 Leave 2 1 8 Leave 1 2 9 Leave 0 3 提示： * 1 <= s.length <= 50 * s 仅由字母 'E' 和 'L' 组成。 * s 表示一个有效的进出序列。
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 通过遍历字符串 s，维护当前候诊室中的人数，并记录最大人数以确定最少椅子数。

算法步骤:
1. 初始化两个变量：current_people 用于记录当前候诊室中的人数，max_people 用于记录最大人数。
2. 遍历字符串 s：
   - 如果字符为 'E'，则 current_people 加 1。
   - 如果字符为 'L'，则 current_people 减 1。
   - 更新 max_people 为 current_people 和 max_people 中的较大值。
3. 返回 max_people 作为最少椅子数。

关键点:
- 通过遍历字符串并维护当前人数和最大人数，可以高效地确定最少椅子数。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串 s 的长度。我们只需要遍历一次字符串。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def min_chairs(s: str) -> int:
    """
    函数式接口 - 计算候诊室中的最少椅子数
    """
    current_people = 0
    max_people = 0
    
    for event in s:
        if event == 'E':
            current_people += 1
        elif event == 'L':
            current_people -= 1
        max_people = max(max_people, current_people)
    
    return max_people


Solution = create_solution(min_chairs)