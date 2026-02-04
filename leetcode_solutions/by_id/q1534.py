# -*- coding:utf-8 -*-
# ============================================================================
# 题目信息
# ============================================================================
"""
题号: 1534
标题: Minimum Number of Frogs Croaking
难度: medium
链接: https://leetcode.cn/problems/minimum-number-of-frogs-croaking/
题目类型: 字符串、计数
"""

# ============================================================================
# 问题描述
# ============================================================================
"""
1419. 数青蛙 - 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。 请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。 要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。 示例 1： 输入：croakOfFrogs = "croakcroak" 输出：1 解释：一只青蛙 “呱呱” 两次 示例 2： 输入：croakOfFrogs = "crcoakroak" 输出：2 解释：最少需要两只青蛙，“呱呱” 声用黑体标注 第一只青蛙 "crcoakroak" 第二只青蛙 "crcoakroak" 示例 3： 输入：croakOfFrogs = "croakcrook" 输出：-1 解释：给出的字符串不是 "croak" 的有效组合。 提示： * 1 <= croakOfFrogs.length <= 105 * 字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k'
"""

# ============================================================================
# 实现思路
# ============================================================================
"""
核心思想: 使用计数器来跟踪每个字符的状态，并确保每个字符的顺序正确。

算法步骤:
1. 初始化五个计数器，分别对应 'c', 'r', 'o', 'a', 'k'。
2. 遍历字符串，根据当前字符更新相应的计数器。
3. 检查每个字符的顺序是否正确，如果不正确则返回 -1。
4. 计算同时发声的青蛙数量的最大值。

关键点:
- 使用计数器来跟踪每个字符的状态。
- 确保每个字符的顺序正确。
"""

# ============================================================================
# 复杂度分析
# ============================================================================
"""
时间复杂度: O(n)，其中 n 是字符串的长度。
空间复杂度: O(1)，只使用了常数级的额外空间。
"""

# ============================================================================
# 代码实现
# ============================================================================

from typing import List, Optional
from leetcode_solutions.utils.linked_list import ListNode
from leetcode_solutions.utils.tree import TreeNode
from leetcode_solutions.utils.solution import create_solution


def minNumberOfFrogs(croakOfFrogs: str) -> int:
    """
    函数式接口 - 返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
    """
    if len(croakOfFrogs) % 5 != 0:
        return -1
    
    count = [0] * 5  # 计数器，分别对应 'c', 'r', 'o', 'a', 'k'
    max_frogs = 0  # 最多同时发声的青蛙数量
    for char in croakOfFrogs:
        idx = "croak".find(char)
        count[idx] += 1
        if idx > 0 and count[idx] > count[idx - 1]:
            return -1
        if idx == 0:
            max_frogs = max(max_frogs, sum(count))
        elif idx == 4:
            for i in range(4):
                count[i] -= 1
    
    if any(count):
        return -1
    return max_frogs


Solution = create_solution(minNumberOfFrogs)